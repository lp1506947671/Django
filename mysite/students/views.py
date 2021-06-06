import json

# Create your views here.
from django.views import View
from django.http.response import JsonResponse, HttpResponse
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
        print(request.body)
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
        return HttpResponse("更新完成")
