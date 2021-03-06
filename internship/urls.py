"""internship URL Configuration

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
from survey import views as survey_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',survey_views.home,name='home'),
    path('create/',survey_views.create,name='create'),
    path('vote/<poll_id>/',survey_views.vote,name='vote'),
    path('results/<poll_id>/',survey_views.results,name='results'),
    path('delete/<poll_id>/',survey_views.delete,name='delete'),
    #path('update/<poll_id>/',survey_views.update,name='update'),
]
