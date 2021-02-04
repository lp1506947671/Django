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
    return HttpResponse(reverse("my_url_controller:reverse") + "\n" + reverse("my_url_controller1:reverse"))


# my_url_controller/my_url_controller_template1/
def my_url_controller_base1_demo(request):
    dict1 = {"variate1": "demo1", "list1": [199, 2, 3], 'filesize': 123456789, "variate_slice": "hello world",
             "list2": [], "demo2": True, "demo3": {"demo3_1": "3_1"}, "demo4": 6
             }
    return render(request, "my_url_controller_template1.html", dict1)


# my_url_controller/my_template_inherit/
def my_template_inherit(request):
    return render(request, "my_template_inherit.html")


# my_url_controller/my_template_include/
def my_template_include(request):
    return render(request, "my_template_include.html")
