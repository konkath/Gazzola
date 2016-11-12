from gazzola.models import Pizza, Topping, Pizzeria


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
