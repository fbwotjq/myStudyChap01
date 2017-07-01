from django.conf.urls import url
from bookmark.views import BookmarkDV, BookMarkLV, ajaxRequest, ajaxOtherRequest, justDirectReturnHtml, justMethodDirectReturnHtml, bookMarkLVFunction, ajax, ajax_json_list

urlpatterns = [
    url(r'^$', BookMarkLV.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
    url(r'^ajax/$', ajaxRequest, name='ajaxRequest'),
    url(r'^ajax/other/$', ajaxOtherRequest, name='ajaxOtherRequest'),
    url(r'^just/direct/return/html/$', justDirectReturnHtml, name='justDirectReturnHtml'),
    url(r'^just/method/direct/return/html/$', justMethodDirectReturnHtml, name='justMethodDirectReturnHtml'),
    url(r'^book/mark/function/(\w+)/$', bookMarkLVFunction, name='bookMarkLVFunction'),
    url(r'^book/mark/ajax/$', ajax, name='ajax'),
    url(r'^book/mark/ajax/json/list/$', ajax_json_list, name='ajax_json_list')
]