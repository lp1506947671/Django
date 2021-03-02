from django.shortcuts import render

# Create your views here.
from my_model.models import Book, Author, Publish


def books(request):
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request, "add_books.html", {"publish_list": publish_list, "author_list": author_list})
