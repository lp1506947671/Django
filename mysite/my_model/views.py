from django.shortcuts import render
from django.http import HttpResponse
from my_model.models import Book, Publish, Author


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
    # book_object.authors.add(auth_obj1, auth_obj2)

    # 绑定方式二
    # book_object = Book.objects.get(title="三国演义")
    # auth_obj1 = Author.objects.get(name="Jason1")
    # auth_obj2 = Author.objects.get(name="Jason2")
    # book_object.authors.add(*[auth_obj1, auth_obj2])

    # 解除关系
    # book_object = Book.objects.get(title="三国演义")
    # book_object.authors.remove(*[1, 2])
    # book_object.authors.clear()

    return HttpResponse("ok")
