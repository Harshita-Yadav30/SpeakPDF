"""
URL configuration for SpeakPDF project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.homeView, name='home'),
    path('feedback', views.feedbackView, name='feedback'),
    path('contact', views.contactView, name='contact'),
    path('audio', views.audioConvertView, name='audio'),
    path('language', views.languageConvertView, name='language'),
    path('login', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('register', views.registerView, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
