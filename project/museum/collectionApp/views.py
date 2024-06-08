from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def collection(request):
    html = '<html><body>藏品</body></html>'
    return HttpResponse(html)


def penmanship(request):
    html = '<html><body>书法</body></html>'
    return HttpResponse(html)


def Bronze_ware(request):
    html = '<html><body>青铜器</body></html>'
    return HttpResponse(html)


def porcelain(request):
    html = '<html><body>瓷器</body></html>'
    return HttpResponse(html)
