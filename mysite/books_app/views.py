import json

from django.http import HttpResponse
from django.shortcuts import render

from books_app.models import User
from my_model.models import Book, Author, Publish


# Create your views here.
def add_books(request):
    if request.method == "POST":
        title = request.POST.get("title")
        price = float(request.POST.get("price"))
        publish_date = request.POST.get("publish_date")
        publish_id = request.POST.get("publish_id")
        authors_id_list = request.POST.get("authors_id_list")
        book_obj = Book.objects.create(title=title, price=price, pub_date=publish_date, publish_id=publish_id)
        book_obj.authors.add(*authors_id_list)
        return HttpResponse("success")

    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request, "add_books.html", {"author_list": author_list, "publish_list": publish_list})


def view_books(request):
    book_list = Book.objects.all().values("id", "title", "price", "price", "pub_date", "publish__name", "authors__name")
    print(book_list)
    return render(request, "view_books.html", {"book_list": book_list})


def change_book(request, edit_book_id, author_name):
    edit_book_obj = Book.objects.filter(pk=edit_book_id, authors__name=author_name).values("title", "price", "pub_date",
                                                                                           "authors__name"
                                                                                           ""
                                                                                           "")
    print(edit_book_obj)
    publish_list = Publish.objects.all()
    author_list = Author.objects.all().values("id", "name")
    print(author_list)
    return render(request, "edit_books.html",
                  {"edit_book_obj": edit_book_obj, "publish_list": publish_list, "author_list": author_list})


def digit_add(request):
    if request.method == "POST":
        n1 = int(request.POST.get("n1"))
        n2 = int(request.POST.get("n2"))
        ret = n1 + n2
        return HttpResponse(ret)

    return render(request, "digit_add.html")


def login(request):
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    user = User.objects.filter(name=user, pwd=pwd).first()
    res = {"user": None, "msg": None}
    if user:
        res["user"] = user.name
    else:
        res["msg"] = "username or password wrong! "
    return HttpResponse(json.dumps(res))


def file_put(request):
    if request.method == "POST":
        print("body_type:", type(request.body))
        print()
        print("POST", request.POST)
        print(request.FILES)
        file_obj = request.FILES.get("avatar")
        with open(file_obj.name, "wb") as f:
            for line in file_obj:
                f.write(line)
        return HttpResponse("ok")
    return render(request, "file_put.html")
