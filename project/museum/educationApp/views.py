from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import ad
from .forms import ResumeForm


# Create your views here.

def culture(request):
    return render(request,'culture.html',{
        'active_menu':'education',
        'sub_menu':'culture',
        })


def history(request):
    adlist = ad.objects.all().order_by('-publishDate')
    if request.method == 'POST':
        resumeForm = ResumeForm(data=request.POST,files=request.FILES)
        if resumeForm.is_valid():
            resumeForm.save()
            return render(request,'success.html',{
        'active_menu':'education',
        'sub_menu':'history',
        })
    else:
        resumeForm = ResumeForm()
    return render(request,'history.html',{
        'active_menu':'education',
        'sub_menu':'history',
        'adlist':adlist,
        'resumeForm' : resumeForm,
        })