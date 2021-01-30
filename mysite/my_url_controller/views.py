import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# /
from django.urls import reverse


def index(request):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "index.html", {"now_time": now_time})


# re_path:简单的路由配置 /my_url_controller/2003/03/03
def my_url_controller_demo1(request, year, month):
    return HttpResponse("re_path:简单的路由配置 %s:%s" % (year, month))


# re_path:有名分组 /my_url_controller/2003/03/1
def my_url_controller_demo2(request, year, month, day):
    return HttpResponse("re_path:有名分组 year=%s:month=%s:day=%s" % (year, month, day))


# my_url_controller/reserve/
def my_url_controller_reverse(request):
    return HttpResponse(reverse("my_url_controller:reverse") + "\n"+reverse("my_url_controller1:reverse"))
