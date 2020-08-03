"""ClassGC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as main_views
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('about/', main_views.about, name='about'),
    path('toc/', main_views.toc, name='toc'),
    path('', main_views.home, name='home'),
    path('uni/', main_views.uni_list, name='uni'),
    path('uni/<str:shortname>/', main_views.class_list, name='class_list'),
    path('uni/<str:shortname>/<str:uclass_id>/', main_views.note_list, name='note_list'),
    path('add_class/', main_views.add_class, name='add_class'),
    path('add_note/', main_views.add_note, name='add_note'),
    path('add_url/', main_views.add_url, name='add_url'),
]
