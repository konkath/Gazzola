from gazzola.models import Pizza


def get_pizzas_from_db():
    return Pizza.objects.all()
