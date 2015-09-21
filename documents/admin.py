from django.contrib import admin

# Register your models here.
from documents.models import Document, Node


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", )


class NodeAdmin(admin.ModelAdmin):
    list_display = ("content", "parent_node", "order", "is_title", "ignore_numbering", "order", "overall_order", "numbering_type")

admin.site.register(Document, DocumentAdmin)
admin.site.register(Node, NodeAdmin)