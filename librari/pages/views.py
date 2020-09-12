from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from Book.models import Book
from Cart.models import Cart
# Create your views here.

def home(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request,"pages/index.html",context)

def detail(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    context = {
        "book":book
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
        "total": cart.get_total()
    }
    return render(request,"pages/cart.html",context)