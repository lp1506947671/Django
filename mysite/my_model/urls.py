#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path

from my_model import views
app_name = "my_model"
urlpatterns = [
    path("", views.index),
]
