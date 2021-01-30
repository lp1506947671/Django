#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path

from my_url_controller import views

app_name = "my_url_controller1"
urlpatterns = [
    path("reserve/", views.my_url_controller_reverse, name="reverse")
]
