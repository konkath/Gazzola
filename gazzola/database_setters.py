from datetime import datetime
from django.contrib.auth.models import User
from gazzola.models import Customer, Address


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
