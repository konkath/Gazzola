from datetime import datetime
from django.contrib.auth.models import User
from gazzola.models import Customer, Address, OrderedPizza, Order, Review


def create_customer(name, surname, email, password, city, house_number, street, postal_code, apt_number):
    user = create_user(email, password)

    if user:
        customer = Customer(user=user, name=name, surname=surname, reg_date=datetime.now(), order_count=0)
        customer.save()

        address = create_address(city, house_number, street, postal_code, apt_number)
        customer.address.add(address)
        return customer
    return None


def create_address(city, house_number, street, postal_code, apt_number):
    address = Address(city=city, postal_code=postal_code, street=street, house_number=house_number,
                      apt_number=apt_number)
    address.save()
    return address


def create_user(email, password):
    user = User.objects.filter(username=email)

    if not user:
        user = User.objects.create_user(email, email, password)
        user.save()

        return user
    return None


def create_ordered_pizza(pizza_name, pizza_size, pizza_toppings):
    ordered_pizza = OrderedPizza(pizza_name=pizza_name, size=pizza_size)
    ordered_pizza.save()

    for topping in pizza_toppings:
        ordered_pizza.toppings.add(topping)

    return ordered_pizza


def create_order(customer, pizzas, address, additional_info):
    order = Order(customer=customer, address=address, additional_info=additional_info, order_date=datetime.now())
    order.save()

    for pizza in pizzas:
        order.pizzas.add(pizza)

    return order


def update_topping_count_in_storage_db(storage, topping_count):
    storage.count = topping_count
    storage.save()


def create_review_db(rating, review):
    review = Review(rating=rating, review=review)
    review.save()

    return review


def update_order_of_review_db(order, review):
    order.review = review
    order.save()
