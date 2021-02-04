#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.urls import path, register_converter

from my_url_controller import views, customiz_path_converter

register_converter(converter=customiz_path_converter.CusPatCon, type_name="yyy")

app_name = "my_url_controller1"
urlpatterns = [
    path("reserve/", views.my_url_controller_reverse, name="reverse"),
    path("customiz_path_converter/<yyy:year>/<yyy:month>/<yyy:day>", views.my_url_controller_demo2),
    path("my_url_controller_template1/", views.my_url_controller_base1_demo),
    path("my_template_inherit/", views.my_template_inherit),
    path("my_template_include/", views.my_template_include)
]
