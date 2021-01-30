from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def my_url_controller2_demo1(request):
    return HttpResponse(reverse("my_url_controller2:reverse"))


def my_url_controller2_demo2(request, year, month, day):
    print("type:%s" % type(year))
    # return HttpResponse(
    #     reverse("my_url_controller2:my_url_controller2_demo2", kwargs={"year": year, "month": month, "day": day}))
    return render(request, "my_url_controller2_demo2.html")
