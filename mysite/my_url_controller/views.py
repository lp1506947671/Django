import datetime

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# /
def index(request):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "index.html", {"now_time": now_time})


# /my_url_controller/2003/03/03/1
def my_url_controller(request, year, month, day):

    return HttpResponse(year+month+day)
