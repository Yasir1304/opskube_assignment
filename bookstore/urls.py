# """bookstore URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
"""bookstore URL Configuration
 
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('book.urls')),
# ]
 
#  book/urls.py:
# Code:
from django.urls import path
from django.contrib.auth import views as auth_views
from book.views import *

from django.views.static import serve
from django.conf.urls import url
from django.conf import settings
 
urlpatterns =[
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('login/', loginPage,name='login'),
    path('viewcart/', viewcart,name='viewcart'),
    path('addbook/', addbook,name='addbook'),
    path('register/', registerPage,name='register'),
    path('logout/', logoutPage,name='logout'),
    path('addtocart/<str:pk>', addtocart,name='addtocart'),
    path('delete/<int:id>',delete,name='name'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
