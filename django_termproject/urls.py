"""django_termproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from loginpage.views import index
from loginpage.views import index2
from loginpage.views import index3
from loginpage.views import index4
from loginpage.views import index5
from loginpage.views import index6
from loginpage.views import sent_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loginpage.urls')),
    path('', index),
    path('page1', index),
    path('page2', index2),
    path('page3', index3),
    path('page4', index4),
    path('page5', index5),
    path('page6', index6),
    path('sentpage', sent_page),
]
