#! /usr/bin/python
# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render_to_response


# table
def search_form(request):
    return render_to_response('search_form.html')


# accept date from table_form
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        message = 'What you are searching for is :' + request.GET['q']
    else:
        message = 'You submit a blank form!'
    return HttpResponse(message)
