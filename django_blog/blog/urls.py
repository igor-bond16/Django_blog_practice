#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 07:10:15 2020

@author: igor
"""

from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^',views.home,name='home'),
        url(r'^([0-9]+)/$',views.home,name='home'),
        url(r'^create/',views.create,name='create'),
        url(r'^edit/([0-9]+)/$',views.edit,name='edit'),
        url(r'^delete/([0-9]+)/$',views.delete,name='delete'),
        url(r'^find/',views.find,name='find'),
        url(r'^check/',views.check,name='check'),
        url(r'^message/',views.message,name='message'),
        url(r'^([0-9]+)/$',views.message,name='message'),
    ]
