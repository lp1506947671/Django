#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from mysite.settings import WHITE_LIST


class MyMiddle1(MiddlewareMixin):
    def process_request(self, request):
        print("MyMiddle1 process_request ... ")
        if request.path in WHITE_LIST:
            return None
        if request.user.is_authenticated:
            return redirect("/my_model/login")

    def process_view(self, request, callback, callback_arg, callback_kwargs):
        print("MyMiddle1 process_view ... ")

    def process_exception(self, request, exception):
        print("MyMiddle1 process_exception ...")
        # return HttpResponse(exception)

    def process_response(self, request, response):
        print("MyMiddle1 process_response ... ")
        return response


class MyMiddle2(MiddlewareMixin):
    def process_request(self, request):
        print("MyMiddle2 process_request ... ")

    def process_view(self, request, callback, callback_arg, callback_kwargs):
        print("MyMiddle2 process_view ... ")

    def process_exception(self, request, exception):
        print("MyMiddle2 process_exception ...")
        return HttpResponse(exception)

    def process_response(self, request, response):
        print("MyMiddle2 process_response ... ")
        return response
