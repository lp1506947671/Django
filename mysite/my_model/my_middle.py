#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddle1(MiddlewareMixin):
    def process_request(self, request):
        print("MyMiddle1 process_request ... ")

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

    def process_exception(self, request,exception):
        print("MyMiddle2 process_exception ...")
        return HttpResponse(exception)

    def process_response(self, request, response):
        print("MyMiddle2 process_response ... ")
        return response
