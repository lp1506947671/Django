import json

# Create your views here.
from django.db import DataError
from django.views import View
from django.http.response import JsonResponse, HttpResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import status
from rest_framework.decorators import action

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.permissions import AllowAny, BasePermission, IsAuthenticated

from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, \
    DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializer, StudentSerializer, StudentModel2Serializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class Student2ViewSet(View):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentModel2Serializer(instance=student, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = StudentModel2Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse("ok")


class StudentView(View):
    def get(self, request):
        student = Student.objects.all()
        serializer = StudentSerializer(instance=student, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        print(request.body)
        data = json.loads(request.body)
        serializer = StudentSerializer(data=data)
        print(f"成功:{serializer.is_valid(raise_exception=True)}")
        print(f"失败:{serializer.errors}")
        data = serializer.save()
        return HttpResponse("生成新数据成功")

    def put(self, request):
        print(request.body)
        data = json.loads(request.body)
        put_id = data.get("id")
        student = Student.objects.get(pk=put_id)
        # 使用partial参数来允许部分字段更新,即使存在required字段没有提交
        serializer = StudentSerializer(instance=student, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        # save中传递的关键字参数在create,和update方法中也可以获取
        serializer.save()
        return Response("ok")


class Student3ViewSet(APIView):

    def get(self, request):
        print(f"Request.query_params{request.query_params}")
        print(f"Request.data{request.data}")
        print(f"Request.getlist{request.query_params.getlist('a')}")
        print(f"Request.get{request.query_params.get('a')}")
        student = Student.objects.all()
        serializer = StudentModel2Serializer(instance=student, many=True)
        response = Response(serializer.data, status=status.HTTP_200_OK, )
        response.set_cookie("username", "abc")
        response["company"] = "Oldboy"
        print(f"response.data{response.data}")
        print(f"response.content{response.content}")
        print(f"response.status_code{response.status_code}")
        return response

    def post(self, request):
        print(f"request.data{request.data}")
        print(f"Request.query_params{request.query_params}")
        data = json.loads(request.body)
        serializer = StudentModel2Serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return HttpResponse("ok")


class Student4ViewSet(GenericAPIView):
    serializer_class = StudentModel2Serializer
    queryset = Student.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return StudentModelSerializer
        else:
            return StudentModel2Serializer

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_object(), many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data, context={})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Student5ViewSet(GenericAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def get(self, request, pk):
        serializer = self.get_serializer(instance=self.queryset.get(pk=pk))
        return Response(serializer.data)

    def put(self, request, pk):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# ----------------------5个视图扩展类 ----------------------

class Student6ModelMixin(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def get(self, request):
        """获取多条数据"""
        return self.list(request)

    def post(self, request):
        return self.create(request)


class Student7ModelMixin(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# ----------------------5个GenericAPIView的视图子类集----------------------
class Student8ModelMixin(ListAPIView, CreateAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class Student9ModelMixin(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


# ----------------------常用的四个视图集----------------------
from rest_framework.viewsets import ViewSet, GenericViewSet, ModelViewSet, ReadOnlyModelViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


# ViewSet
class Student10APIViewSet(ViewSet):

    def list(self, request):
        """获取多条数据"""
        student_list = Student.objects.all()
        serializer = StudentModelSerializer(instance=student_list, many=True)
        return Response(serializer.data)

    def get_one(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentModelSerializer(instance=student)
        return Response(serializer.data)


# GenericViewSet
class Student11APIViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


# ModelViewSet
class Student12APIViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()

    @action(methods=['get'], detail=True)
    def login(self, request, pk):
        raise DataError("数据库错误")
        return Response("测试数据login")

    # detail为False 表示路径名格式应该为 router_stu/get_new_5/
    @action(methods=['get'], detail=False)
    def get_new_5(self, request):
        """获取最新添加的5个学生信息"""
        return Response("测试数据get_new_5")


# ReadOnlyModelViewSet
class Student13APIViewSet(ReadOnlyModelViewSet):
    throttle_classes = (AnonRateThrottle,)
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()


class Student14APIViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()
    throttle_classes = (UserRateThrottle,)
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ("sex", "class_num")
    ordering_fields = ['id']


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.username == "xiaopanwye":
            return True


class Student15APIViewSet(ModelViewSet):
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "jason"
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()
    permission_classes = [CustomPermission]


class StandardPageNumberPagination(PageNumberPagination):
    # 默认每一页显示的数量
    page_size = 2
    page_size_query_param = "size"
    max_page_size = 10
    page_query_param = 'p'


class StandardLimitOffsetPagination(LimitOffsetPagination):
    # 默认每一页显示的数量
    default_limit = 2
    limit_query_param = "size"
    offset_query_param = "start"


class Student16APIViewSet(ModelViewSet):
    serializer_class = StudentModelSerializer
    queryset = Student.objects.all()
    pagination_class = StandardLimitOffsetPagination
