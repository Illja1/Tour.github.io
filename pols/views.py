from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Tour, Category, Reviews
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserLoginForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string



def tour_book(request,detail_id):

    return render(request, 'pols/tour_book.html')
def search(request):
    object = Tour.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        searched = request.POST.get('searched')
        header = Tour.objects.filter(title__contains=searched)

        return render(request,'pols/search.html',{'searched':searched,'header':header,'categories': categories,
                   'title':"Hot Tour 202",
                   'object':object,
                   'title1':'Назва туру',
                   'description':'Опис',
                   'photo':'Фото',

})
    else:
        return render(request,'pols/search.html',{})

def user_logout(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Register complete')
            return redirect('login')
        else:
            messages.error(request, 'Register not complete')
    else:
            form = UserRegisterForm()
    return render(request, 'pols/register.html',{"form":form,'title':'Tour'})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
            form = UserLoginForm()
    return render(request, 'pols/login.html',{"form":form,'title':'Tour'})


def landing(request):
    object = Tour.objects.all()
    categories = Category.objects.all()
    context ={'categories': categories,
               'title':"Hot Tour 202",
               'object':object,
               'title1':'Назва туру',
               'description':'Опис',
               'photo':'Фото'
               }
    return render(request,'pols/landing.html',context=context)

def get_category(request,category_id):
    object = Tour.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
    'object':object,
    'categories': categories,
    'category':category,
    'title':'Катерогії',
    }

    return render(request,'pols/category.html',context=context)

#
