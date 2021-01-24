import datetime

from django.shortcuts import render


# Create your views here.
def index(request):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, "index.html", {"now_time": now_time})
