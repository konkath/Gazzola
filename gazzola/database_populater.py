import datetime

from .models import *


# The one and only purpose of this file is to keep unified database between members
def populate():
    addr1 = Address(city='Wroclaw', postal_code=10900, street='Sliczna', house_number=10, apt_number=5)
    addr2 = Address(city='Wroclaw', postal_code=10900, house_number=10)
    addr3 = Address(city='Wroclaw', postal_code=10500, street='Slaba', house_number=10)
    addr4 = Address(city='Wroclaw', postal_code=10200, house_number=10, apt_number=5)
    addr5 = Address(city='Wroclaw', postal_code=10100, street='Pizzeriana', house_number=2, apt_number=5)
    addr6 = Address(city='Wroclaw', postal_code=10100, street='Mariana', house_number=15, apt_number=5)

    addr1.save()
    addr2.save()
    addr3.save()
    addr4.save()
    addr5.save()
    addr6.save()

    usr1 = User.objects.create_user('john', 'john@john.com', 'johnpassword')
    usr2 = User.objects.create_user('ania', 'ania@ania.com', 'aniapassword')
    usr3 = User.objects.create_user('tomek', 'tomek@tomek.com', 'tomekpassword')
    usr4 = User.objects.create_user('stefan', 'stefan@stefan.com', 'stefanpassword')

    cust1 = Customer(user=usr1, name='John', surname='John', reg_date=datetime.datetime.now(), order_count=10)
    cust1.save()
    cust1.address.add(addr1, addr2)
    cust2 = Customer(user=usr2, name='Ania', surname='Rak', reg_date=datetime.datetime.now(), order_count=0)
    cust2.save()
    cust1.address.add(addr2)
    cust3 = Customer(user=usr3, name='Toemk', surname='Turbo', reg_date=datetime.datetime.now(), order_count=2)
    cust3.save()
    cust1.address.add(addr3)
    cust4 = Customer(user=usr4, name='Stefan', surname='Duzy', reg_date=datetime.datetime.now(), order_count=4)
    cust4.save()
    cust1.address.add(addr4)

    rev1 = Review(customer=cust1, rating=5, review='best pizza ever')
    rev2 = Review(customer=cust3, rating=4)

    rev1.save()
    rev2.save()

    top1 = Topping(name='pieczarki', price=2)
    top2 = Topping(name='ser', price=1)
    top3 = Topping(name='kurczak', price=2)
    top4 = Topping(name='wolowina', price=2)
    top5 = Topping(name='ananas', price=1)
    top6 = Topping(name='salami', price=2)

    top1.save()
    top2.save()
    top3.save()
    top4.save()
    top5.save()
    top6.save()

    pizza1 = Pizza(pizza_name='margarita', price=15)
    pizza1.save()
    pizza1.toppings.add(top1, top2)

    pizza2 = Pizza(pizza_name='hawajska', price=17)
    pizza2.save()
    pizza2.toppings.add(top1, top2, top5)

    pizza3 = Pizza(pizza_name='wiejska', price=17)
    pizza3.save()
    pizza3.toppings.add(top2, top3, top4, top6)

    str1 = Storage(topping=top1, count=45)
    str2 = Storage(topping=top2, count=10)
    str3 = Storage(topping=top3, count=15)
    str4 = Storage(topping=top4, count=20)
    str5 = Storage(topping=top5, count=30)
    str6 = Storage(topping=top6, count=8)

    str1.save()
    str2.save()
    str3.save()
    str4.save()
    str5.save()
    str6.save()

    str7 = Storage(topping=top1, count=5)
    str8 = Storage(topping=top2, count=10)
    str9 = Storage(topping=top3, count=12)
    str10 = Storage(topping=top4, count=30)
    str11 = Storage(topping=top5, count=20)
    str12 = Storage(topping=top6, count=8)

    str7.save()
    str8.save()
    str9.save()
    str10.save()
    str11.save()
    str12.save()

    sto1 = Storeroom()
    sto1.save()
    sto1.storage.add(str1, str2, str3, str4, str5, str6)

    sto2 = Storeroom()
    sto2.save()
    sto2.storage.add(str7, str8, str9, str10, str11, str12)

    pizzer1 = Pizzeria(name='Gazzola Pizza', address=addr5, storeroom=sto1)
    pizzer2 = Pizzeria(name='Gazzola Home', address=addr6, storeroom=sto2)

    pizzer1.save()
    pizzer2.save()

    pr1 = Promo(discount=10, valid_from=datetime.datetime.now(), valid_to=datetime.datetime.now())
    pr2 = Promo(pizza=pizza1, discount=20, valid_from=datetime.datetime.now(), valid_to=datetime.datetime.now())

    pr1.save()
    pr2.save()
