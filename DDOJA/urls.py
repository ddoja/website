"""DDOJA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from webpage import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^quienes-somos/', views.about_us, name='about_us'),
    url(r'^asesores/', views.lawyers, name='lawyers'),
    url(r'^servicios/', views.services, name='services'),
    url(r'^consulta-legal/', views.consulting, name='consulting'),
    url(r'^seminarios/', views.courses, name='courses'),
    url(r'^contactanos/', views.contact_us, name='contact_us'),
    url(r'^consulta-online/', views.online_consulting, name='online_consulting'),
]
