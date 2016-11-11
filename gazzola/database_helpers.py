from gazzola.database_getters import get_topping_from_db, get_pizza_from_db


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
