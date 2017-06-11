from django.conf.urls import url
from bookmark.views import BookmarkDV, BookMarkLV

urlpatterns = [
    url(r'bookmark/$', BookMarkLV.as_view(), name='index'),
    url(r'bookmark/(?P<pk>\d+)/$', BookmarkDV.as_view(), name='detail'),
]