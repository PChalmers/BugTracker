"""BugTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from . import views

#from tracker.views import projectCreate_view


urlpatterns = [
    path('login', views.loginToAccount),
    path('', views.home_page),
    path('createAccount', views.accountCreate_view),
    path('createProject', views.projectCreate_view),
    path('createRecord', views.recordCreate_view),
    path('createComment', views.commentCreate_view),
    path('about', views.about_page),
    path('contact', views.contact_page),
    path('admin/', admin.site.urls),

]








