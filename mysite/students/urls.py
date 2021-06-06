#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path("student/", views.Student2ViewSet.as_view())
]
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('student', views.StudentView)
# urlpatterns += router.urls
