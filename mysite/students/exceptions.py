#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from rest_framework.views import exception_handler as drf_exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    # 先让drf进行异常判断
    response = drf_exception_handler(exc, context)
    if response is None:

        if isinstance(exc, DatabaseError):
            view = context.get('view')
            print(f"数据库报错,{view}:{exc}")
            return Response({"detail": "服务器内部错误"}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
        if isinstance(exec, ZeroDivisionError):
            view = context.get("view")
            print(f"0不能做为除数!{view}:{exc}")
            return Response({"detail": "服务器内部错误"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
