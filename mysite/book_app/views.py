from django.http import HttpResponse
from django.shortcuts import render
from book_app.models import BookApp


# Create your views here.


def add_book(request):
    # 生成一个csrf_token键值对加到到context中，后面form表单提交验证用
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        book_obj = BookApp.objects.create(title=title, price=price, pub_date=date, publish=publish)
        return HttpResponse("ok")

    return render(request, "add_book.html")
