from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from Book.models import Book
from Cart.models import Cart
from .forms import Search
# Create your views here.

form = Search()

def home(request):
    context = {
        "books": Book.objects.all(),
        "form": form
    }
    return render(request,"pages/index.html",context)

def detail(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    context = {
        "book":book,
        "form":form
    }
    return render(request,"pages/product.html",context)

def addToCart(request,book_id):
    cart = get_object_or_404(Cart,cart=User.objects.get(pk=request.user.id))
    book = get_object_or_404(Book,pk=book_id)
    book.cart.add(cart)
    return HttpResponseRedirect("/cart")

def removeFromCart(request,book_id):
    cart = get_object_or_404(Cart,cart=User.objects.get(pk=request.user.id))
    book = get_object_or_404(Book,pk=book_id)
    book.cart.remove(cart)
    return HttpResponseRedirect("/cart")

def cart(request):
    cart = get_object_or_404(Cart,cart=request.user)
    context = {
        "books": cart.book_set.all(),
        "total": cart.get_total(),
        "form":form
    }
    return render(request,"pages/cart.html",context)

def searchview(request):
    if request.method == 'POST':
        form = Search(request.POST)
        if form.is_valid():
            searchText = form.cleaned_data["searchText"]
            books = Book.objects.filter(titulli__contains=searchText) | Book.objects.filter(autori__contains=searchText)
    else:
        form = Search()
        return HttpResponseRedirect('/')
    context = {
        'form': form,
        'books': books
    }
    return render(request, "pages/index.html", context)
