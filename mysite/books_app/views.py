import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect

from books_app.models import User
from my_model.models import Book, Author, Publish
from books_app.models import Book as Books


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


def paginator(request):
    a = Books.objects.all().order_by("pk")
    paginator1 = Paginator(a, 3)
    print("数据总数:", paginator1.count)
    print("总页数:", paginator1.num_pages)
    print("页码列表:", paginator1.page_range)
    page1 = paginator1.page(1)
    print("下一页数:", page1.next_page_number())
    print("下一页", page1.has_next())
    page2 = paginator1.page(2)
    print("上一页数:", page2.previous_page_number())
    print("上一页:", page2.has_previous())

    # 抛错
    # page=paginator.page(12)   # error:EmptyPage
    # page=paginator.page("z")   # error:PageNotAnInteger

    current_page_num = int(request.GET.get("page", 1))
    try:
        current_page = paginator1.page(current_page_num)
        print("object_list", current_page.object_list)
    except EmptyPage as e:
        current_page = paginator1.page(1)
    except PageNotAnInteger as e:
        current_page = paginator1.page(paginator1.count)

    # 需求:总页数54,使其永远只显示11页
    if paginator1.num_pages > 11:

        if current_page_num - 5 < 1:
            page_range = range(1, 12)
        elif current_page_num + 5 > paginator1.num_pages:
            page_range = range(paginator1.num_pages - 10, paginator1.num_pages + 1)

        else:
            page_range = range(current_page_num - 5, current_page_num + 6)
    else:
        page_range = paginator1.page_range

    # page_range = paginator1.page_range
    dict1 = {
        "page_range": page_range,
        "current_page_num": current_page_num,
        "current_page": current_page,
    }

    return render(request, "paginator.html", dict1)


from django import forms
from django.core.exceptions import ValidationError

wid_01 = forms.TextInput(attrs={"class": "form-control"})
wid_02 = forms.PasswordInput(attrs={"class": "form-control"})


class UserForm(forms.Form):
    name = forms.CharField(max_length=32, label="用户名", widget=wid_01)
    pwd = forms.CharField(label="密码", widget=wid_02)
    r_pwd = forms.CharField(label="确认密码", widget=wid_02)
    email = forms.EmailField(label="邮件", widget=wid_01)
    tel = forms.CharField(max_length=32, label="手机号码", widget=wid_01)

    def clean_name(self):
        """局部钩子"""
        val = self.cleaned_data.get("name")
        if val.isdigit():
            return val
        else:
            raise ValidationError("用户名不能是纯数字!")

    def clean(self):
        """全局钩子"""
        pwd = self.cleaned_data.get("pwd")
        r_pwd = self.cleaned_data.get("r_pwd")

        if pwd == r_pwd:
            return self.cleaned_data
        else:
            raise ValidationError('两次密码不一致!')


def register(request):
    if request.method == "POST":
        dict1 = {}
        user = UserForm(request.POST)
        if user.is_valid():
            print(user.cleaned_data)
        else:
            dict1["clean_error"] = user.errors.get("__all__")
        dict1["user"] = user
        return render(request, "register.html", dict1)
    user = UserForm()

    return render(request, "register.html", {"user": user})


import datetime


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = User.objects.filter(name=user, pwd=pwd).first()
        if user:
            response = HttpResponse("登录成功!")
            response.set_cookie("is_login", True)
            response.set_cookie("username", user.name)
            return response

    return render(request, "login.html")


def index(request):
    is_login = request.COOKIES.get("is_login")
    if is_login:
        username = request.COOKIES.get("username")
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        last_time = request.COOKIES.get("last_visit_time", "")
        response = render(request, "index.html", {"username": username, "last_time": last_time, "now_time": now})
        response.set_cookie("last_visit_time", now)
        return response

    else:
        return redirect("/login/")
