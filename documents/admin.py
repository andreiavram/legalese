from django.contrib import admin

# Register your models here.
from documents.models import Document, Node, DocumentProvider


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", )


class NodeAdmin(admin.ModelAdmin):
    list_display = ("content", "parent_node", "order", "is_title", "ignore_numbering", "order", "overall_order", "numbering_type")


class DocumentProviderAdmin(admin.ModelAdmin):
    list_display = ("name", )


admin.site.register(Document, DocumentAdmin)
admin.site.register(Node, NodeAdmin)
admin.site.register(DocumentProvider, DocumentProviderAdmin)
