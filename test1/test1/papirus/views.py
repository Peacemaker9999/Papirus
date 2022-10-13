from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from elasticsearch_dsl.response import Response
from django.contrib.auth import authenticate

from .models import *


#
# def index(request):
#     users = User.objects.all()
#     staff = User.objects.filter(is_staff=True)
#     context = {'users': users, 'staff': staff}
#     return render(request, 'home/index.html', context)


# class DataMixin(object):
#     def get_context_data(self, **kwargs):
#         context = super()
#         context['staff'] = User.objects.filter(is_staff=True)
#         return context
#
#
# class LoginUser(DataMixin, LoginView):
#     form_class = AuthenticationForm
#     template_name = 'papirus/login.html'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Авторизация')
#         return dict(list(context.items()) + list(c_def.items()))
#
#     def get_success_url(self):
#         return reverse_lazy('home')


def accounts(request):
    return render(request, 'registration/base.html')


def login(request):
    return render(request, 'registration/login.html')


def base(request):
    return render(request, 'registration/base.html')


def members(request):
    memberss = Papirus.objects.all()
    return render(request, {'members': memberss})


def about(request):
    posts = Papirus.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'papirus/about.html', context=context)


def main_page(request):
    return render(request, 'papirus/main_page.html')


def add_document(request):
    return render(request, 'papirus/add_document.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not Found</h1>')
