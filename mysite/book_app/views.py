from django.http import HttpResponse
from django.shortcuts import render, redirect
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
        return redirect("/book_app/view/")

    return render(request, "add_book.html")


def view_book(request):
    book_list = BookApp.objects.all()

    return render(request, "view_book.html", context={"book_list": book_list})


def delete_book(request, id):
    BookApp.objects.filter(id__exact=id).delete()
    return redirect("/book_app/view/")


def edit_book(request, id):
    book_object = BookApp.objects.filter(id__exact=id).first()
    if request.method == "POST":
        title = request.POST.get("title")
        price = request.POST.get("price")
        date = request.POST.get("date")
        publish = request.POST.get("publish")
        BookApp.objects.filter(id__exact=id).update(title=title, price=price, pub_date=date,
                                                    publish=publish)
        return redirect("/book_app/view/")

    return render(request, "edit_book.html", context={"book_object": book_object})
