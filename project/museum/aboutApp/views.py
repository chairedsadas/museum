from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.
def about(request):
    html = "<html><body>关于</body></html>"
    return HttpResponse(html)


def introduce(request):
    html = "<html><body>总体介绍</body></html>"
    return HttpResponse(html)


def leader(request):
    html = "<html><body>领导</body></html>"
    return HttpResponse(html)
