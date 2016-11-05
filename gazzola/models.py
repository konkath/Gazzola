from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User


class Address(models.Model):
    city = models.CharField(max_length=64)
    postal_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    street = models.CharField(max_length=64, null=True)
    house_number = models.CharField(max_length=4)
    apt_number = models.CharField(max_length=4, null=True)

    def __str__(self):
        if self.apt_number:
            return self.city + '(' + self.postal_code + ') ' + self.street + ' ' + self.house_number + '/' + \
                   self.apt_number
        return self.city + '(' + self.postal_code + ') ' + self.street + ' ' + self.house_number


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=64)
    email = models.EmailField()
    reg_date = models.DateField()
    order_count = models.PositiveIntegerField()
    address = models.ManyToManyField(Address)

    def __str__(self):
        return self.name + ' ' + self.surname


class Review(models.Model):
    customer = models.ForeignKey(Customer)
    rating = models.IntegerField()
    review = models.CharField(max_length=255)

    def print_customer(self):
        return self.customer.name + ' ' + self.customer.surname

    def __str__(self):
        return self.print_customer() + ' ' + str(self.rating)


class Topping(models.Model):
    name = models.CharField(max_length=16, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=32, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.pizza_name


class Storeroom(models.Model):
    toppings = models.ForeignKey(Topping)
    count = models.PositiveIntegerField(validators=[MaxValueValidator(999)])

    def __str__(self):
        return str(self.pk)


class Pizzeria(models.Model):
    name = models.CharField(max_length=32, unique=True)
    address = models.ForeignKey(Address)
    storeroom = models.ForeignKey(Storeroom)

    def __str__(self):
        return self.name


class Promo(models.Model):
    pizza = models.ForeignKey(Pizza)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateField()
    valid_to = models.DateField()

    def __str__(self):
        return str(self.valid_from) + '-' + str(self.valid_to)


class OrderedPizza(models.Model):
    pizza = models.ForeignKey(Pizza)
    size = models.PositiveIntegerField(validators=[MaxValueValidator(4)])

    def __str__(self):
        return str(self.pk)


class Order(models.Model):
    customer = models.ForeignKey(Customer)
    pizza = models.ForeignKey(OrderedPizza)
    address = models.ForeignKey(Address)
    additional_info = models.CharField(max_length=128)
    order_date = models.DateField()

    def print_customer(self):
        return self.customer.name + ' ' + self.customer.surname

    def __str__(self):
        return self.print_customer() + ' (' + self.order_date + ')'
