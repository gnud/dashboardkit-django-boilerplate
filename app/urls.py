# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from app.views import MyPage, IndexPage

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    path(r'promotions/', MyPage().as_view()),
    path(r'products/', IndexPage().as_view()),
    re_path(r'^.*\.*', views.pages, name='pages'),

]
