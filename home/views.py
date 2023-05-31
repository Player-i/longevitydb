from django.shortcuts import render
from django.http import HttpResponse
from .models import Study
# Create your views here.


def home(request):
    
    studies = Study.objects.all()
    context = {"studies": studies }
    return render(request, "home.html", context=context)

def sleep(request):
    
    studies = Study.objects.all()
    context = {"studies": studies }
    return render(request, "sleep.html", context=context)

def supplements(request):
    
    studies = Study.objects.all()
    context = {"studies": studies }
    return render(request, "supplements.html", context=context)

def diet(request):
    
    studies = Study.objects.all()
    context = {"studies": studies }
    return render(request, "diet.html", context=context)

def see_study(request, slug):

    study = Study.objects.get(slug=slug)
    context = {"study": study}
    return render(request, "study.html", context=context)
