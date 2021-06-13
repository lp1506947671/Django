#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path, re_path
from . import views

urlpatterns = [
    path("student/", views.Student3ViewSet.as_view()),
    path("student4/", views.Student4ViewSet.as_view()),
    re_path(r"^student5/(?P<pk>\d+)/$", views.Student5ViewSet.as_view()),
    # ----------------------5个视图扩展类 ----------------------
    path("student6/", views.Student6ModelMixin.as_view()),
    re_path(r"^student7/(?P<pk>\d+)/$", views.Student7ModelMixin.as_view()),
    # ----------------------5个GenericAPIView的视图子类集----------------------
    path("student8/", views.Student8ModelMixin.as_view()),
    re_path(r"^student9/(?P<pk>\d+)/$", views.Student9ModelMixin.as_view()),
]
