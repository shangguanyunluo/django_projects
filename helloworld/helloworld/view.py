#! /usr/bin/python
# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("hello world!")


def person(request):
    context = {}
    context['name'] = 'zhangsan'
    context['age'] = 23
    return render(request, 'person.html', context)


def base(request):
    return render(request, 'base.html', None)


def hello2(request):
    return render(request, 'hello.html', None)
