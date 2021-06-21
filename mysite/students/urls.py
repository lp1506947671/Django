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
    path("student10/", views.Student10APIViewSet.as_view({"get": "list"})),
    re_path(r"^student10/(?P<pk>\d+)/$", views.Student10APIViewSet.as_view({"get": "get_one"})),
    path("student11/", views.Student11APIViewSet.as_view({"get": "list"})),
    re_path(r"^student11/(?P<pk>\d+)/$", views.Student11APIViewSet.as_view({"get": "retrieve"})),
    # path("student12/", views.Student12APIViewSet.as_view({"get": "list"})),
    # re_path(r"^student12/(?P<pk>\d+)/$", views.Student12APIViewSet.as_view({"get": "retrieve", "post": "create"})),
    path("student13/", views.Student13APIViewSet.as_view({"get": "list", "post": "create"})),
    re_path(r"^student13/(?P<pk>\d+)/$", views.Student13APIViewSet.as_view({"get": "retrieve"})),

]
from rest_framework import routers

routers = routers.SimpleRouter()
routers.register("student12", views.Student12APIViewSet, "student12_1")
routers.register("student14", views.Student14APIViewSet, "student14_1")
routers.register("student15", views.Student15APIViewSet, "student15_1")
routers.register("student16", views.Student16APIViewSet, "student16_1")
print(routers.urls)
urlpatterns += routers.urls
