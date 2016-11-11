import json
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect
from gazzola.database_helpers import count_pizza_price


@csrf_protect
def save_basket_session(request):
    cart = None
    if request.is_ajax() and request.POST:
        pizza_name = request.POST['pizza_name']
        pizza_size = request.POST['pizza_size']
        pizza_toppings = request.POST.getlist('toppings[]')

        price = count_pizza_price(pizza_name, pizza_toppings)
        my_pizza = [pizza_name, pizza_size, pizza_toppings, str(price)]

        if 'cart' in request.session:
            cart = request.session['cart']
            cart.append(my_pizza)
        else:
            cart = [my_pizza]
        request.session['cart'] = cart

    return HttpResponse(json.dumps(cart), content_type='application/json')


@csrf_protect
def get_basket_session(request):
    cart = None

    if request.is_ajax() and 'cart' in request.session:
        cart = request.session.get('cart')

    return HttpResponse(json.dumps(cart), content_type='application/json')


@csrf_protect
def set_pizzeria_session(request):
    if request.is_ajax and request.POST:
        request.session['pizzeria'] = request.POST['pizzeria_name']
    return HttpResponse(content_type='application/json')


@csrf_protect
def get_pizzeria_session(request):
    if request.is_ajax and 'pizzeria' in request.session:
        pizzeria = request.session.get('pizzeria')
    else:
        pizzeria = None
        request.session['pizzeria'] = pizzeria

    return HttpResponse(json.dumps(pizzeria), content_type='application/json')
