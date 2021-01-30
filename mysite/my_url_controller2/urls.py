#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path, re_path

from my_url_controller2 import views

app_name = 'my_url_controller2'
urlpatterns = [
    path("reserve/", views.my_url_controller2_demo1, name="reverse"),
    re_path("(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]+)/$", views.my_url_controller2_demo2,
            name="my_url_controller2_demo2")
]
