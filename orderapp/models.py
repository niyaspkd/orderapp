from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Products(models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    code = models.CharField(max_length=100, null=True, blank=True)
    price= models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    features = models.TextField( null=True, blank=True)
    inventory = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

class Customer(models.Model):

    username = models.CharField(unique=True,max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField( null=True, blank=True)
    mobile =  PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.name

def create_user(sender, instance, **kwargs):

    User.objects.update_or_create(username=instance.username)

post_save.connect(create_user, sender=Customer)

class Cart(models.Model):
     products = models.OneToOneField(Products,on_delete=models.CASCADE)
     amount = models.CharField(max_length=100, null=True, blank=True)
     quantity = models.IntegerField()
     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


     def save(self, *args, **kwargs):
          self.instance.customer = self.request.user
          self.instance.products.inventory = self.instance.products.inventory - 1
          self.instance.save()
          self.instance.products.save()
          super(Model, self).save(*args, **kwargs)

class Order(models.Model):

    products = models.ManyToManyField(Cart)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)

   
def post_order(sender, instance, **kwargs):
    total  = 0
    for product in instance.products:
      total = total + product.price * quantity
    payment_amount = total / discount 
    instance.total_amount = total
    instance.payement_amount = payment_amount
    instance.save()

post_save.connect(post_order, sender=Customer)


   