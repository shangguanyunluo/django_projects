#! /usr/bin/python
# coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render
from TestModel.models import Test


def add(request):
    test1 = Test(name='testdb')
    test1.save()
    return HttpResponse('Success to add data.')


def list(request):
    context = {}

    context['list'] = Test.objects.all()

    context['first'] = Test.objects.filter(id=1)
    print context['first']

    context['single'] = Test.objects.get(id=1)

    context['offset'] = Test.objects.order_by('name')[0:2]

    return render(request, 'testdb.html', context)


def update(request):
    context = {}

    test = Test.objects.get(id=2)
    test.name = 'Lisi'
    test.save()
    context['single'] = Test.objects.get(id=2)

    # Test.objects.filter(id=1).update(name='Google')
    # Test.objects.all().update(name='Google')
    return render(request, 'testdb.html', context)


def delete(request):
    test = Test.objects.get(id=3)
    test.name = 'Lisi'
    test.delete()
    context = {}

    context['list'] = Test.objects.all()
    return render(request, 'testdb.html', context)
