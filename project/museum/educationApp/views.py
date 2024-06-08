from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def culture(request):
    html = '<html><body>文化</body></html>'
    return HttpResponse(html)


def history(request):
    html = '<html><body>历史</body></html>'
    return HttpResponse(html)


def education(request):
    html = '<html><body>教育</body></html>'
    return HttpResponse(html)
