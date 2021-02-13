from django.shortcuts import render
from django.http import HttpResponse
from my_model.models import Book


# Create your views here.
def index(request):
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
    Book.objects.create(title="go宝典", state=True, price=300, publish="人民出版社", pub_date="2012-12-12")
    Book.objects.filter(price__exact=300).update(title="php")
    Book.objects.filter(title="php").delete()

    return HttpResponse("ok")
