import logging
from random import randint

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from gazzola.database_getters import get_toppings_from_db
from gazzola.database_helpers import get_pizza_with_real_price, get_pizzeria_names, get_order_history_for_user, \
    get_address_for_user, place_order
from gazzola.database_populater import populate
from gazzola.database_setters import create_customer


def login_view(request):
    # If user is logged in already redirect to home
    if request.user.is_authenticated():
        HttpResponseRedirect('/')

    # Submit button
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        # Try to authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            # Check if user is active
            if user.is_active:
                # Login user and redirect him to home
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'login.html', {'object': 'Your account is inactive'})
        else:
            return render(request, 'login.html', {'object': 'Your credentials are invalid'})

    return render(request, 'login.html')


def pizzeria_view(request):
    if 'pizzeria' in request.session:
        return render(request, 'pizzeria.html', {'pizzas': get_pizza_with_real_price(),
                                                 'toppings': get_toppings_from_db()})
    else:
        return HttpResponseRedirect('/')


def index_content_view(request):
    pizzeria_names = get_pizzeria_names()
    return render(request, 'index.html', {'pizzerias': pizzeria_names,
                                          'pizzerias_count': len(pizzeria_names)})


@login_required
def place_order_view(request):
    if 'pizzeria' in request.session:
        if request.POST:
            address_id = request.POST['address']
            delivery_type = request.POST['delivery_type']
            additional_info = request.POST['additional_info']

            result = place_order(request.user, request.session['pizzeria'], request.session['cart'], address_id,
                                 delivery_type, additional_info)

            if result[0] == 0:
                return render(request, 'order_summary.html', {'order': result[1], 'timer': randint(30, 60)})
            elif result[0] == 3:
                return render(request, 'order.html', {'addresses': get_address_for_user(request.user),
                                                      'status': result[0], 'missing_toppings': result[1]})
            else:
                return render(request, 'order.html', {'addresses': get_address_for_user(request.user),
                                                      'status': result[0], 'message': result[1]})

        return render(request, 'order.html', {'addresses': get_address_for_user(request.user)})
    else:
        return HttpResponseRedirect('/')


def register_view(request):
    if request.POST:
        logging.debug(request.POST)
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        city = request.POST['city']
        house_number = request.POST['house_number']
        postal_code = request.POST['postal_code']
        street = request.POST['street']
        apt_number = request.POST['apt_number']

        customer = create_customer(name, surname, email, password, city, house_number, street, postal_code, apt_number)

        if customer:
            return render(request, 'register.html', {'register_status': 1})
        return render(request, 'register.html', {'register_status': 0})

    return render(request, 'register.html')


@login_required
def user_panel_view(request):
    logging.debug(request.user)
    return render(request, 'user_panel.html', {'order_history': get_order_history_for_user(request.user)})


@login_required
def logout_view(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect('/')


# Debug purpose
@login_required
def populate_database(request):
    populate()
    return render(request, 'index.html')
