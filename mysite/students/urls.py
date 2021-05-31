#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = [
    path("student/", views.StudentView.as_view())
]
# router = DefaultRouter()
# router.register('student', views.StudentView)
# urlpatterns += router.urls
