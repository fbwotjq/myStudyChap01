# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import json

from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.views.generic import ListView, DetailView

from bookmark.form import SearchForm
from bookmark.models import Bookmark

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
logger.addHandler(streamHandler)

class BookMarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

'''
    여러개의 결과(리스트도 포함)를 리턴하는 예제
'''
def bookMarkLVFunction(request, query):
    try:
        bookMarkList = Bookmark.objects.filter(title__contains=query)
    except:
        raise Http404('can not find bookMark => ' + query)

    template = get_template('bookmark/bookmark_page.html')
    variables = {
        'query': query,
        'bookmarks': bookMarkList
    }
    output = template.render(variables, request)
    return HttpResponse(output)

'''
    바로 html을 생성해서 리턴하는 예제
'''
def justDirectReturnHtml(request):
    output = '''
    <html> <head><title>%s</title></head>
    <body> <h1>%s</h1><p>%s</p>
    </body> </html>
    ''' % (
        '장고 | 북마크',
        '장고 북마크에 오신 것을 환영합니다.', '여기에 북마크를 저장하고 공유할 수 있습니다!'
    )
    return HttpResponse(output)

'''
    여러개의 일반적인 결과를 던진다.
'''
def justMethodDirectReturnHtml(request):
    template = get_template('bookmark/main_page.html')
    variables = {
        'head_title': 'django bookmark',
        'page_title': 'u welcome django world',
        'page_body': 'save and share ur bookmark',
    }
    output = template.render(variables, request)
    return HttpResponse(output)

'''
    일반적인 아주 간단한 ajax 예제
'''
def ajaxRequest(request):
    query = request.GET.get('query', '')
    data = {
        'is_taken': Bookmark.objects.filter(title__contains=query).exists()
    }
    return JsonResponse(data)

'''
    살짝 ajax 응용, validation 관련 응용, 로거를 사용한다.
    그리고 dict을 이용하여 json으로 리턴한다.
'''
def ajaxOtherRequest(request):

    query = request.GET.get('query', 'None')
    logger.debug("[ajaxOtherRequest] query => " + query)

    validationStatus = SearchForm({'query': query})
    logger.debug(validationStatus)

    #bookmarks = Bookmark.objects.filter(title__contains=query)[:2]
    bookmarks = Bookmark.objects.filter(title__contains=query)
    logger.debug(bookmarks)

    bookmarksResult = bookmarks.values('pk', 'title', 'url')
    bookmarksResult = list(bookmarksResult)
    logger.debug(bookmarksResult)

    return JsonResponse({
        'isExist': bookmarks.exists(),
        'bookmarks': bookmarksResult
    })

def ajax(request):
    data = {}
    data['something'] = 'useful'
    return HttpResponse(json.dumps(data), content_type = "application/json")

def ajax_json_list(request):
    query = request.GET.get('query', '')
    bookmarks = Bookmark.objects.filter(title__contains=query)
    #bookmarksResult = bookmarks.values('title', 'url').values_list()
    data = serializers.serialize("json", bookmarks)
    return HttpResponse(data, content_type='application/json')


'''
    view 쪼개기
'''