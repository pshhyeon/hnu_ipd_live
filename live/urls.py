"""
URL configuration for live project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from live import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.main),
    path('test_page', views.test_page),
    path('door_lock_page', views.door_lock_page),
    path('login_page', views.login_page),
    path('login_act', views.login_act),
    path('home', views.home),
    path('save_password', views.save_password),
    path('password_list_page', views.password_list_page),
    path('door_pass', views.door_pass),
]
