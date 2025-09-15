"""
URL configuration for sign_language project.

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
from django.urls import path

from sign_language_app.views import *

urlpatterns = [
    path('login',Login_View.as_view(), name='login'),
    path('replay',Send_replay.as_view(), name='replay'),
    path('complaints',View_Complaints.as_view(), name='complaints'),
    path('feedback',View_Feedback.as_view(), name='feedback'),
    path('view_user',View_User.as_view(),name='view_user'),

    #################################################################

    path('user_complaints',Send_Complaints.as_view(),name='user_complaints'),
    path('user_feedback',Send_Feedback.as_view(),name='user_feedback'),
    path('user_registration',User_Registration.as_view(),name='user_registration'),
]
