#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path, re_path

from book_app import views

app_name = "my_model"
urlpatterns = [
    path("add/", views.add_book),
    path("view/", views.view_book),
    re_path(r"delete/(\d+)", views.delete_book)
]
