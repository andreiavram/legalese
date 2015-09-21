from django.db import models
from django.db.models import permalink
from legalese.utils import int_to_roman


class FakeNode(object):
    def __init__(self, node_type=None, numbering_type=None, numbering_format=None, title_children=False):
        super(FakeNode, self).__init__()
        self.is_node_marker = True
        self.node_type = node_type if node_type else "start"
        self.numbering_type = numbering_type
        self.numbering_format = numbering_format
        self.title_children=title_children


class Document(models.Model):
    title = models.CharField(max_length=1024)
    parent_document = models.ForeignKey("documents.Document", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True)

    root_numbering = models.CharField(max_length=255, default="none")
    root_numbering_format = models.CharField(max_length=255, default="%%i")

    def __unicode__(self):
        return u"%s" % self.title

    def process_node(self, node):
        node_list = [node, ]
        if node.child_nodes.count():
            node_kwargs = dict(
                node_type="start",
                numbering_type=node.numbering_type,
                numbering_format=node.numbering_format,
                title_children=node.all_children_are_titles()
            )

            node_list.append(FakeNode(**node_kwargs))

        for child in node.child_nodes.all():
            node_list.extend(self.process_node(child))

        if node.child_nodes.count():
            node_list.append(FakeNode(node_type="end"))
        return node_list

    def get_node_list(self, root_node=None):
        if not self.nodes.exists():
            return []

        start_nodes = self.nodes.all() if root_node is None else [root_node, ]

        ref_node = start_nodes[0]
        node_kwargs = dict(
            node_type="start",
            numbering_type=ref_node.numbering_type if root_node is None else "none",
            numbering_format=ref_node.numbering_format,
            title_children=ref_node.all_children_are_titles()
        )
        nodes = [FakeNode(**node_kwargs), ]
        if root_node is None:
            for node in start_nodes.filter(parent_node__isnull=True):
                nodes.extend(self.process_node(node))
        else:
            nodes.extend(self.process_node(root_node))
        nodes.append(FakeNode(node_type="end"))
        return nodes

    @permalink
    def get_absolute_url(self):
        return "document_detail", [], {"pk": self.id}


class Node(models.Model):
    NUMERAL = "numbers"
    ROMAN_NUMERAL = "roman"
    LETTERS = "letters"
    NONE = "none"
    DASHES = "dashes"
    NUMBERING_TYPES = ((NUMERAL, u"Numbers"),
                       (ROMAN_NUMERAL, u"Roman numbers"),
                       (LETTERS, u"Letters"),
                       (DASHES, u"Dashes"),
                       (NONE, u"No numbering"))

    document = models.ForeignKey("documents.Document", related_name="nodes")
    content = models.TextField()
    parent_node = models.ForeignKey("documents.Node", null=True, blank=True, related_name="child_nodes")
    is_title = models.BooleanField(default=False)

    order = models.IntegerField(default=1)
    numbering_type = models.CharField(max_length=255, choices=NUMBERING_TYPES, default="none")
    numbering_format = models.CharField(max_length=255, default="%%i")

    overall_order = models.IntegerField(null=True, blank=True)
    overall_numbering_type = models.CharField(max_length=255, choices=NUMBERING_TYPES,  blank=True, null=True, default="none")
    overall_numbering_format = models.CharField(max_length=255, default="%%i", blank=True, null=True)
    ignore_numbering = models.BooleanField(default=False)
    alternate_marker = models.CharField(max_length=10, null=True, blank=True)
    depth = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content

    @classmethod
    def process_numbering_type(cls, numbering, order):
        if numbering == cls.NUMERAL:
            return "%s" % order
        if numbering == cls.ROMAN_NUMERAL:
            return int_to_roman(order)
        if numbering == cls.LETTERS:
            return chr(ord('A') + order - 1)
        return ""

    def process_numbering_format(self, num_type, num_format):
        final_string = num_format
        final_string = final_string.replace("%%i", self.process_numbering_type(num_type, self.order))

        if "%%pp" in final_string and self.depth > 2:
            parent = self.parent_node.parent_node
            final_string = final_string.replace("%%pp", self.process_numbering_type(parent.parent_node.numbering_type, parent.order))
        if "%%p" in final_string and self.depth > 1:
            parent = self.parent_node
            final_string = final_string.replace("%%p", self.process_numbering_type(parent.parent_node.numbering_type, parent.order))

        return final_string

    def get_prefix(self):
        if not self.is_title:
            return ""

        if self.parent_node is None:
            return self.process_numbering_format(self.document.root_numbering, self.document.root_numbering_format)

        return self.process_numbering_format(self.parent_node.numbering_type, self.parent_node.numbering_format)

    def all_children_are_titles(self):
        return all([a.is_title for a in self.child_nodes.all()])

    def get_closest_overall_parent(self):
        if self.overall_order:
            return self

        node = self
        while node.parent_node is not None:
            node = node.parent_node
            if node.overall_order:
                return node

        return self

    def has_overall_parent(self):
        if self.overall_order:
            return True

        return self.get_closest_overall_parent() != self