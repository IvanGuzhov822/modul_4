from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
def page1(request):
    return HttpResponse('Это новая страница')

def top_sellers(request):
    return render(request , 'top-sellers.html')