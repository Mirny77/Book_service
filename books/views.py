from django.shortcuts import render
from books.models import *


def book(request, product_id):
    product = Book.objects.get(id=product_id)


    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


    return render(request, 'books/book.html', locals())

def home(request):
    book_images = Book.objects.all()


    return render(request, 'home.html', locals())
