from gazzola.database_getters import get_topping_from_db, get_pizza_from_db, get_pizzas_from_db, get_pizzerias_from_db


def count_pizza_price(pizza_name, pizza_toppings):
    pizza_db = get_pizza_from_db(pizza_name)

    price = 0
    if pizza_db:
        price = pizza_db.price
        for topping in pizza_toppings:
            topping_db = get_topping_from_db(topping)

            if topping_db:
                price += topping_db.price
    return price


class RealPizza:
    pizza_name = None
    price = 0
    toppings = None

    def __init__(self, pizza):
        self.pizza_name = pizza.pizza_name
        self.toppings = pizza.toppings
        self.price = self.count_price(pizza.price)

    def count_price(self, price):
        for topping in self.toppings.all():
            price += topping.price
        return price


def get_pizza_with_real_price():
    pizzas = get_pizzas_from_db()

    real_pizzas = []
    for pizza in pizzas:
        real_pizzas.append(RealPizza(pizza))

    return real_pizzas


def get_pizzeria_names():
    pizzerias_db = get_pizzerias_from_db()

    names = []
    for pizzeria in pizzerias_db:
        names.append(pizzeria.name)
    return names
