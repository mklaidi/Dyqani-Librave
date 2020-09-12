from django.urls import path
from . import views

app_name = "pages"
urlpatterns = [
    path('',views.home,name="home"),
    path('book/<int:book_id>/',views.detail,name="detail"),
    path('book/<int:book_id>/add/',views.addToCart,name="addToCart"),
    path('book/<int:book_id>/remove/',views.removeFromCart,name="removeFromCart"),
    path('cart',views.cart,name="cart")
]