from django.shortcuts import render
from rest_framework import generics
from .models import Products, Customer, Order, Cart
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductSerializer, CustomerSerializer, OrderSerializer,CartSerializer
# Create your views here.

from rest_framework.views import APIView

class ProductView(generics.CreateAPIView, generics.ListAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer
#    permission_classes = [IsAdminUser]
    

 
class CustomerView(generics.CreateAPIView, generics.ListAPIView):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]


class OrderView(generics.CreateAPIView, generics.ListAPIView):
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]
    search_fields = ['customer__name', 'customer__mobile']

class CartView(generics.CreateAPIView, generics.ListAPIView):
    
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filter_backends = [DjangoFilterBackend]
    permission_classes = [IsAuthenticated]

    search_fields = ['customer__name', 'customer__mobile']

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        print(self)
        user = self.request.user
        
        return Cart.objects.filter(customer__user=user)

@login_required
class Summary(APIView):
    

    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        order = self.get_object(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
