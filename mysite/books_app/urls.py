#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path, re_path

from books_app import views

app_name = "books_app"
urlpatterns = [
    path("", views.books),
    # re_path(r"delete/(\d+)", views.delete_book),
]
