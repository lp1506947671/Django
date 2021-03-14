#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path, re_path

from books_app import views

app_name = "books_app"

urlpatterns = [
    re_path(r"add/", views.add_books),
    re_path(r"view/", views.view_books),
    re_path(r'(\d+)/([0-9a-zA-Z]{1,20})/change/$', views.change_book),
    path('', views.digit_add),
    path('login', views.login),
    path("file_form", views.file_put),
    path("paginator", views.paginator),
    path("register", views.register)
]
