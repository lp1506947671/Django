import json

# Create your views here.
from django.views import View
from django.http.response import JsonResponse, HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import Student
from .serializers import StudentModelSerializer, StudentSerializer


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


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
        print(f"成功:{serializer.is_valid()}")
        print(f"失败:{serializer.errors}")
        return HttpResponse("ok")
