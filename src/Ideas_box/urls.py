"""Ideas_box URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from authentication.views import login_view , logout_user , register
from box.views import create_ideas_box , lists_box , vote
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("login/", login_view, name="login"),
    path('logout/', logout_user, name='logout'),
    path("register/", register, name="register"),
    path("create_box/", create_ideas_box, name="create_box"),
    path("list_box/", lists_box, name="list_box"),
    path('vote/<int:box_id>/<str:vote_type>/', vote, name='vote'),
]
