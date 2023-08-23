from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm2
from django.urls import reverse
from django.core.exceptions import ValidationError


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

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm2(request.POST, request.FILES)
        if form.is_valid():
            adv = Advertisement(**form.cleaned_data)
            if adv.title[0] == '?':
                raise ValidationError("Заголовок не может начинаться с вопросительного знака")


            else:
                adv.user = request.user
                adv.save()
                url = reverse('main-page')
                return redirect(url)
            
    else:
        form = AdvertisementForm2()




    context = {'form': form}

    return render(request, 'advertisement-post.html', context)