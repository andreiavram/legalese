from django.conf.urls import patterns, include, url
from django.contrib import admin
from documents.views import DocumentList, DocumentDetail, NodeDetail

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^document/list/$', DocumentList.as_view(), name="document_list"),
    url(r'^document/(?P<slug>[-_\w]i-am +)/$', DocumentDetail.as_view(), name="document_detail"),
    url(r'^node/(?P<pk>\d+)/$', NodeDetail.as_view(), name="node_detail"),
    url(r'^$', DocumentList.as_view(), name="index"),
)

