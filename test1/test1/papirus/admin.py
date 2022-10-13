from django.contrib import admin
from .models import Papirus

admin.site.register(Papirus)

from django.contrib.auth import authenticate, login, logout

user = authenticate(username='john', password='secret')


def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        pass


def logout_view(request):
    logout(request)
    # Redirect to a success page.
