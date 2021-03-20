from django.contrib import auth

from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min, Count
from django.shortcuts import render, redirect
from django.http import HttpResponse
from my_model.models import Book, Publish, Author, AuthorDetail, Emp


# Create your views here.
def index1(request):
    # 1.添加表记录
    # book_obj = Book.objects.create(title="python宝典", state=True, price=100, publish="苹果出版社", pub_date="2012-12-12")
    # book_obj1 = Book.objects.create(title="go宝典", state=True, price=200, publish="人民日报出版社", pub_date="2012-12-12")

    # 2.查询表记录
    # print("****all****:", Book.objects.all())
    # print("****get****:", Book.objects.get(id=1))

    # 3.模糊查询
    # print(Book.objects.filter(price__gt=100))
    # print(Book.objects.filter(title__startswith="py"))
    # print(Book.objects.filter(title__icontains="H"))
    # print(Book.objects.filter(price__in=[100, 200]))
    # print(Book.objects.filter(pub_date__year=2012,pub_date__month=12))

    # 4.修改,删除操作
    # Book.objects.create(title="go宝典", state=True, price=300, publish="人民出版社", pub_date="2012-12-12")
    # Book.objects.filter(price__exact=300).update(title="php")
    # Book.objects.filter(title="php").delete()

    # ------------多表操作之一对多添加记录---------------
    # 绑定方式一
    # pub_obj = Publish.objects.create(name="人民出版社", city="背景", email="beijingchubanshe@qq.com")
    # book_object = Book.objects.create(title="红楼梦", pub_date="2021-12-12", price=300, publish=pub_obj)

    # 绑定方式二
    # pub_obj = Publish.objects.create(name="湖南出版社", city="长沙", email="hunanchubanshe@qq.com")
    # book_object = Book.objects.create(title="三国演义", pub_date="2020-10-10", price=300, publish_id=pub_obj.id)

    # ------------多表操作之多对多添加记录---------------
    # 绑定方式一
    # auth_obj1 = Author.objects.create(name="Jason1", age=16, authorDetail_id=1)
    # auth_obj2 = Author.objects.create(name="Jason2", age=17, authorDetail_id=2)
    # book_object = Book.objects.filter(title="红楼梦").first()
    # print(type(book_object.publish))
    # print(type(book_object.publish_id))
    # book_object.authors.add(auth_obj1, auth_obj2)

    # 绑定方式二
    # book_object = Book.objects.get(title="三国演义")
    # print(book_object.authors.all())
    # auth_obj1 = Author.objects.get(name="Jason1")
    # auth_obj2 = Author.objects.get(name="Jason2")
    # book_object.authors.add(*[auth_obj1, auth_obj2])

    # 解除关系
    # book_object = Book.objects.get(title="三国演义")
    # book_object.authors.remove(*[1, 2])
    # book_object.authors.clear()
    # ------------基于对象的跨表查询---------------
    # ------------基于对象的跨表查询一对一多--------------
    # 正向
    # a = Book.objects.get(title="西游记")
    # print(a.publish)
    # 反向
    # b = Publish.objects.get(name="湖南出版社")
    # print(b.book_set.all())
    # ------------基于对象的跨表查询一对一--------------
    # 正向
    # a = Author.objects.get(name="Jason1")
    # print(a.authorDetail.addr)
    # 反向
    # b = AuthorDetail.objects.get(addr="a")
    # print(b.author.name)
    # ------------基于对象的跨表查询一对多--------------
    # 正向
    # a = Author.objects.get(name="Jason1")
    # print(a.authorDetail.addr)
    # 反向
    # b = AuthorDetail.objects.get(addr="a")
    # print(b.author.name)
    # a = Publish.objects.filter(name="人民出版社").values("book__title", "book__price")
    # print(a)
    # a = Book.objects.filter(publish__name="人民出版社").values("title", "price")
    # print(a)
    # a = Book.objects.filter(authors__name="Jason1").values("title")
    # print(a)
    # a = Author.objects.filter(name="Jason1").values("authorDetail__telephone")
    # print(a)
    # a = AuthorDetail.objects.filter(author__name="Jason1").values("telephone")
    # print(a)
    # a = Book.objects.filter(publish__name="人民出版社").values("title", "authors__name")
    # print(a)
    # a = Publish.objects.filter(name="人民出版社").values("book__title", "book__authors__name")
    # print(a)
    # a = Author.objects.filter(book__publish__name="人民出版社").values("book__title", "name")
    # print(a)
    # a = Book.objects.filter(authors__authorDetail__addr__startswith="a").values("title")
    # print(a)
    # a = Author.objects.filter(authorDetail__addr__startswith="a").values("book__title", "book__publish__name")
    # print(a)
    # ret = Book.objects.all().aggregate(Avg("price"), Max("price"), Min("price"))
    # print(ret)

    # ret = Publish.objects.values("id").annotate(c=Count('book__title')).values_list("name", "c")
    # print(ret)
    # ret = Book.objects.values("authors").annotate(book_price=Max("price")).values("authors__name", "book_price")
    # print(ret)
    # ret = Author.objects.values("pk").annotate(book_price=Max("book__price")).values("name", "book_price")
    ret = Book.objects.values("id").annotate(author_count=Count("authors")).values("title", "author_count")
    print(ret)
    return HttpResponse("ok")


from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = auth.authenticate(username=user, password=pwd)
        if user:
            auth.login(request, user)
            next_url = request.GET.get("next", "/my_model/index")
            return redirect(next_url)
    return render(request, 'my_model/login.html')


def index(request):
    return render(request, "my_model/index.html")


def logout(request):
    auth.logout(request)
    return redirect("/my_model/login")


def reg(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        user = User.objects.create_user(username=user, password=pwd)
        return redirect("/my_model/login")
    return render(request, "my_model/reg.html")


@login_required
def order(request):
    return render(request, "my_model/order.html")


def my_middle(request):
    print("views")
    return HttpResponse("ok")
