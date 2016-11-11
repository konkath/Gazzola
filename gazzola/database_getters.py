from gazzola.models import Pizza, Topping


def get_pizzas_from_db():
    return Pizza.objects.all()


def get_toppings_from_db():
    return Topping.objects.all()
