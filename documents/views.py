from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from documents.models import Document, Node


class DocumentList(ListView):
    template_name = "documents/document_list.html"
    model = Document


class DocumentDetail(DetailView):
    template_name = "documents/document_detail.html"
    model = Document

    def get_context_data(self, **kwargs):
        data = super(DocumentDetail, self).get_context_data(**kwargs)
        data['nodes'] = self.object.get_node_list()
        return data


class NodeDetail(DetailView):
    template_name = "documents/node_detail.html"
    model = Node

    def get_context_data(self, **kwargs):
        data = super(NodeDetail, self).get_context_data(**kwargs)
        art_node = self.object.get_closest_overall_parent()
        data['nodes'] = self.object.document.get_node_list(art_node)
        return data



