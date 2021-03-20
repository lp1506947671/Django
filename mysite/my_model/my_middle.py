#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class MyMiddle1(MiddlewareMixin):
    def process_request(self, request):
        print("MyMiddle1 process_request ... ")


    def process_response(self, request, response):
        print("MyMiddle1 process_response ... ")
        return response


class MyMiddle2(MiddlewareMixin):
    def process_request(self, request):
        print("MyMiddle2 process_request ... ")
        return HttpResponse("中断")

    def process_response(self, request, response):
        print("MyMiddle2 process_response ... ")
        return response
