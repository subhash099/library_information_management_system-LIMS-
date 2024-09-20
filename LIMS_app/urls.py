"""
URL configuration for lims_portal project.

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

from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('home', home),
    path('readers',readers_tab,name="readers"),
    path('<int:id>',readers_info,name="readers_info"),
    path('add/',add,name="add"),
    path('books/',books,name="books"),
   
    path('delete/<int:id>/',delete_reader,name="deletereaders"),
    path('edit/<int:id>/',edit,name="edit"),
]
