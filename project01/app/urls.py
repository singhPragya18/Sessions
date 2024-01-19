from .views import *
from django.urls import path

urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('services/',services,name='services'),
    # path('dashboard/',dashboard,name='dashboard'),
    path('login/',login,name='login'),
    path('registration/',registration,name='registration'),
    path('savedata/',savedata,name='savedata'),
    path('login1/',login1,name='login1'),
    path('logindata',logindata,name='logindata'),
    path('datadelete',datadelete,name='datadelete')
]