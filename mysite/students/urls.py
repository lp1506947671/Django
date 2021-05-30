#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = []
router = DefaultRouter()
router.register('students', views.StudentViewSet)
urlpatterns += router.urls
