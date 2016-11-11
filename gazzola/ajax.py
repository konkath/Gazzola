import json

from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def save_basket_session(request):
    cart = None
    if request.is_ajax() and request.POST:
        pizza_name = request.POST['pizza_name']
        pizza_size = request.POST['pizza_size']
        pizza_toppings = request.POST.getlist('toppings[]')

        cart = request.session.get['cart']
        if cart:
            cart.append([pizza_name, pizza_size, pizza_toppings])
        else:
            cart = [[pizza_name, pizza_size, pizza_toppings]]
        request.session['cart'] = cart

    return HttpResponse(json.dumps(cart), content_type='application/json')


@csrf_protect
def get_basket_session(request):
    cart = None

    if request.is_ajax() and request.GET:
        cart = request.session.get['cart']

    return HttpResponse(json.dumps(cart), content_type='application/json')
