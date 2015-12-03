from django.shortcuts import render

__author__ = 'Kami Wan'


def index(request):
    return render(request, 'base.html')
