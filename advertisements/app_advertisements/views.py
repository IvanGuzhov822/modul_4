from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm2
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()


def index(request):


    title = request.GET.get('query')


    if title:
        ads = Advertisement.objects.filter(title__icontains = title)
    else:
        ads = Advertisement.objects.all()



    if request.user.is_authenticated == False:


        context = {'advertisements' : ads, 'not_auth' : True, 'title' : title}
    else:
        context = {'advertisements' : ads, 'not_auth' : False, 'title' : title}


    return render(request, 'app_advertisements/index.html', context)
def page1(request):
    return HttpResponse('Это новая страница')

def top_sellers(request):

    
    if request.user.is_authenticated:
        users = User.objects.annotate(
        adv_count = Count('advertisement')
    ).order_by('-adv_count')
        return render(request , 'app_advertisements/top-sellers.html', {'auth' : True, 'users' : users})
    else:
       users = User.objects.annotate(
        adv_count = Count('advertisement')
    ).order_by('-adv_count')
       return render(request , 'app_advertisements/top-sellers.html', {'users' : users}) 
    


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


    if request.user.is_authenticated:
        context = {'form': form, 'auth' : True}
    else:
        context = {'form': form}







    return render(request, 'app_advertisements/advertisement-post.html', context)

def advertisement_detail(request, pk):
    ads = Advertisement.objects.get(id = pk)

    context = {'advertisement' : ads}

    return render(request, 'app_advertisements/advertisement.html', context)