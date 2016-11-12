from gazzola.models import Pizza, Topping, Pizzeria, Order, Customer


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
    customer_db = Customer(user=user)

    if customer_db:
        return customer_db
    return None


def get_orders_for_customer_from_db(customer):
    order_db = Order(customer=customer)

    if order_db:
        return order_db
    return None
