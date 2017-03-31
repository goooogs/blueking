# -*- coding: utf-8 -*-

from common.mymako import render_mako_context

# Create your views here.

def index(request):
	return render_mako_context(request, '/dbaux/index.html', { 'items': [] })

