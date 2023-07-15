from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # root of this app (pages)
    path('about', views.about, name='about')
]