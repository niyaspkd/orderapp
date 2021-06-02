from django.contrib import admin
from django.urls import path, include
from .views import ProductView, CustomerView, OrderView, CartView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductView.as_view()),
    path('customers/', CustomerView.as_view()),
    path('orders/', OrderView.as_view()),
    path('cart/', CartView.as_view()),
    path('summary/<int:pk>/', OrderView.as_view()),



]