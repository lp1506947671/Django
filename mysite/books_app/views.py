from django.http import HttpResponse
from django.shortcuts import render
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


def change_book(request, edit_book_id,author_name):
    edit_book_obj = Book.objects.filter(pk=edit_book_id , authors__name=author_name).values("title", "price", "pub_date","authors__name"
                                                                                                                         ""
                                                                                                                         "")
    print(edit_book_obj)
    publish_list = Publish.objects.all()
    author_list = Author.objects.all().values("id", "name")
    print(author_list)
    return render(request, "edit_books.html",
                  {"edit_book_obj": edit_book_obj, "publish_list": publish_list, "author_list": author_list})
