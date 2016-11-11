"""overhours_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from gazzola import ajax
from . import views

app_name = 'gazzola'
urlpatterns = [
    url(r'^populate_database', views.populate_database, name='populate_database'),
    url(r'^pizzeria', views.pizzeria_view, name='pizzeria'),

    # Ajax
    url(r'^ajax/save_basket_session/', ajax.save_basket_session),
    url(r'^ajax/get_basket_session/', ajax.get_basket_session),

    url(r'^$', views.index_view, name='index'),
    url(r'^register', views.register_view, name='register'),
]
