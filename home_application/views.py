# -*- coding: utf-8 -*-

from common.mymako import render_mako_context
from django.http import HttpResponse

def index(request):
    '''
    Hello World
    '''
    return HttpResponse('ID: lekoood<br />QQ: @□》:______T。<br />Hello World!')


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/home.html')


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


'''
Preview page
'''
def preview(request):
    if request.method == "POST":
        return HttpResponse('congratulation！')
    else:
        return render_mako_context(request, '/home_application/blueking_preview.html')
