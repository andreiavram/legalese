from django.core.management.base import BaseCommand
import os
import re
from documents.models import Node, Document, DocumentProvider


class Command(BaseCommand):
    def handle(self, *args, **options):
        # if len(args) < 1:
        #     self.stderr.write(u"Need file to open!\n")
        #     return

        # if not os.path.exists(args[0]):
        #     self.stderr.write(u"File to open does not exist / is not accessible!\n")
        #     return

        with open("/vagrant/statut2.txt", "rb") as f:
            lines = f.readlines()

        title = "Statut"
        document = Document.objects.create(title=u"Parsed document (%s)" % title,
                                           provider=DocumentProvider.objects.all().first(),
                                           slug="statut-%d" % (Document.objects.count() + 1, ))

        parent = None
        number_of_tabs = 0
        last_node = None
        order_on_levels = {0: 0, "art": 0}

        for line in lines:
            tabs = len(re.findall("^(\t*)", line, re.UNICODE)[0])
            if tabs > number_of_tabs:
                parent = last_node
                number_of_tabs = tabs
                order_on_levels[tabs] = 1
                pass
            elif tabs < number_of_tabs:
                for i in range(number_of_tabs - tabs):
                    if parent is None:
                        break
                    parent = parent.parent_node
                number_of_tabs = tabs
                order_on_levels[tabs] += 1
            else:
                order_on_levels[tabs] += 1

            overall_numbering_type = None

            content = line.strip()
            overall_order = None
            if content.startswith("art:"):
                content = content[4:]
                overall_numbering_type = "art"
                order_on_levels["art"] += 1
                overall_order = order_on_levels["art"]

            is_title = False
            if content.startswith("title:"):
                content = content[len("title:"):]
                is_title = True

            ignore_numbering = False
            if content.startswith("skip:"):
                content = content[len("skip:"):]
                ignore_numbering = True
                order_on_levels[tabs] -= 1

            alternate_marker = None
            if content.startswith("alternate("):
                alternate_marker = re.findall(r"alternate\(([^\)]+)\):", content)
                alternate_marker = alternate_marker[0] if alternate_marker else ""
                content = content[len("alternate:()") + len(alternate_marker):]

                overall_order -= 1
                order_on_levels["art"] -= 1

            markers = ["numbers", "letters", "roman", "dashes"]
            numbering_type = "none"
            for m in markers:
                if content.startswith("%s:" % m):
                    content = content[len(m) + 1:]
                    numbering_type = m
                    break

            numbering_format = "%%i"
            if content.startswith("format("):
                matches = re.findall(r"format\(([^\)]+)\):", content)
                match = matches[0] if matches else ""
                content = content[len("format:()") + len(match):]
                numbering_format = match if match else None

            node = Node.objects.create(document=document, content=content,
                                       order=order_on_levels[tabs], parent_node=parent,
                                       overall_numbering_type=overall_numbering_type,
                                       overall_order=overall_order, is_title=is_title,
                                       ignore_numbering=ignore_numbering, numbering_type=numbering_type,
                                       alternate_marker=alternate_marker if alternate_marker else None,
                                       numbering_format=numbering_format, depth=number_of_tabs)
            last_node = node




