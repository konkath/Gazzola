from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render

from gazzola.database_getters import get_pizzas_from_db
from gazzola.database_populater import populate


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
    return render(request, 'pizzeria.html', {'pizzas', get_pizzas_from_db()})


@login_required
def logout_view(request):
    if request.user.is_authenticated():
        logout(request)

    return HttpResponseRedirect('/')


def index_view(request):
    return render(request, 'index.html')


@login_required
def populate_database(request):
    populate()
    return render(request, 'index.html')
