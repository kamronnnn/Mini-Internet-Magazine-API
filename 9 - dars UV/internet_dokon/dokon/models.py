from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=5)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


class OrderProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.phone_number




