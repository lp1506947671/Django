import json

# Create your views here.
from django.views import View
from django.http.response import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
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
