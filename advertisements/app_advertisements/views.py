from django.shortcuts import render
from django.http import HttpResponse
from .models import Advertisement

def index(request):

    ads = Advertisement.objects.all()

    context = {
        'advertisements' : ads
    }

    return render(request, 'index.html', context)
def page1(request):
    return HttpResponse('Это новая страница')

def top_sellers(request):
    return render(request , 'top-sellers.html')