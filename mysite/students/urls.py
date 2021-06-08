#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("student/", views.Student3ViewSet.as_view()),
    path("student4/", views.Student4ViewSet.as_view()),
    re_path(r"^student5/(?P<pk>\d+)/$", views.Student5ViewSet.as_view()),
]