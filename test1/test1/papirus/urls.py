from django.urls import path, include

from .views import *

urlpatterns = [
    # path('', LoginUser.as_view(), name='login'),
    # path('', login, name='home'),
    path('', login),
    path('members/', members),
    # path('login/', LoginUser.as_view(), name='login')
]
