from django.urls import path
from .views import BaseView, AboutView, CookiesView, ConditionsView

urlpatterns =[
    path("", BaseView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('cookies', CookiesView.as_view(), name='cookies'),
    path('conditions', ConditionsView.as_view(), name='conditions'),
    
   
   ]