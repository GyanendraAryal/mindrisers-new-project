from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # on_delete = models.CASCADE:- deletes all the related data
    # on_delete = models.PROTECT:- first checks if there are any data related to foreign data if yes it doesn't deletes if not deletes.
    # on_delete = SET_NULL:- sets other datas related to foregin key data with null after deletion of foreign data.
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Table(models.Model):
    num = models.CharField(max_length=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.num}"


class Order(models.Model):
    STATUS_CHOICE = [
        ("P", "Pending"),
        ("C", "Completed"),
        ("D", "Delivered"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True, blank=True, default=1)
    total_price = models.FloatField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default="P")
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s order"


class OrderMenu(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    menu = models.ForeignKey(Menu, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.order.user.username}'s order menu"
