from gazzola.models import Pizza, Topping, Pizzeria, Order, Customer, Address, Storage


def get_pizzas_from_db():
    return Pizza.objects.all()


def get_toppings_from_db():
    return Topping.objects.all()


def get_pizzerias_from_db():
    return Pizzeria.objects.all()


def get_topping_from_db(name):
    topping = Topping.objects.filter(name=name)

    if topping:
        return topping[0]
    return None


def get_pizza_from_db(name):
    pizza = Pizza.objects.filter(pizza_name=name)

    if pizza:
        return pizza[0]
    return None


def get_customer_for_user_from_db(user):
    customer_db = Customer.objects.filter(user=user)

    if customer_db:
        return customer_db
    return None


def get_orders_for_customer_from_db(customer):
    order_db = Order.objects.filter(customer=customer)

    if order_db:
        return order_db
    return None


def get_addresses_for_customer_from_db(customer):
    address = Address.objects.filter(customer=customer)

    if address:
        return address
    return None


def get_pizzeria_by_name_from_db(pizzeria_name):
    pizzeria = Pizzeria.objects.filter(name=pizzeria_name)

    if pizzeria:
        return pizzeria[0]
    return None


def get_address_by_id_from_db(address_id):
    address = Address.objects.filter(pk=address_id)

    if address:
        return address[0]
    return None


def get_storage_by_id_from_db(storage_id):
    storage = Storage.objects.filter(pk=storage_id)

    if storage:
        return storage[0]
    return None
