from gazzola.database_getters import get_topping_from_db, get_pizza_from_db, get_pizzas_from_db, get_pizzerias_from_db, \
    get_customer_for_user_from_db, get_orders_for_customer_from_db, get_addresses_for_customer_from_db, \
    get_pizzeria_by_name_from_db, get_address_by_id_from_db
from gazzola.database_setters import create_ordered_pizza, create_order


def count_pizza_price(pizza_name, pizza_toppings, pizza_size):
    pizza_db = get_pizza_from_db(pizza_name)

    price = 0
    if pizza_db:
        price = pizza_db.price
        for topping in pizza_toppings:
            topping_db = get_topping_from_db(topping)

            if topping_db:
                price += topping_db.price
        price = count_price_depending_on_size(pizza_size, price)
    return price


def count_price_depending_on_size(size, price):
    if size == '1':
        return float(price) * 0.75
    elif size == '3':
        return float(price) * 1.25
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


def get_order_history_for_user(user):
    customer = get_customer_for_user_from_db(user)

    if customer:
        return get_orders_for_customer_from_db(customer)
    return None


def get_address_for_user(user):
    customer = get_customer_for_user_from_db(user)

    if customer:
        return get_addresses_for_customer_from_db(customer)
    return None


def convert_string_topping_to_db(toppings):
    if type(toppings) is str:
        return get_topping_from_db(toppings)

    toppings_db = []
    for topping in toppings:
        toppings_db.append(get_topping_from_db(topping))
    return toppings_db


def place_order(user, pizzeria_name, basket, address_id, delivery_type, additional_info):
    pizzeria_db = get_pizzeria_by_name_from_db(pizzeria_name)
    if not pizzeria_db:
        return [1, pizzeria_name]

    customer_db = get_customer_for_user_from_db(user)
    if not customer_db:
        return [2, user]

    toppings = dict()
    for storage in pizzeria_db.storeroom.storage.all():
        toppings[storage.topping.name] = storage.count

    missing_toppings = []
    for item in basket:  # [pizza_name, pizza_size, pizza_toppings, str(price)]
        for topping in item[2]:
            if topping in toppings:
                toppings[topping] -= 1

                if toppings[topping] < 0:
                    missing_toppings.append(topping)

    if missing_toppings:
        return [3, missing_toppings]

    if delivery_type == 'delivery':
        address = get_address_by_id_from_db(address_id)
    elif delivery_type == 'takeout':
        address = pizzeria_db.address
    else:
        return [4, delivery_type]

    total_price = 0
    ordered_pizzas = []
    for item in basket:
        total_price += float(item[3])
        ordered_pizzas.append(create_ordered_pizza(item[0], item[1], convert_string_topping_to_db(item[2])))

    order = create_order(customer_db[0], ordered_pizzas, address, additional_info)
    return [0, order]

