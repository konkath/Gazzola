$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken",
                $('input[name="csrfmiddlewaretoken"]').val());
        }
    }
});

jQuery.validator.addMethod('postal_code', function (value, element) {
    return this.optional(element) || !!value.trim().match(/^[0-9]{2}-[0-9]{3}$/);
}, 'Invalid postal code');

function addTopping(cell) {

    $(cell).parent().children().get(1).innerHTML = $(cell).parent().children().get(1).innerHTML / 1 + 1;
}

function removeTopping(cell) {

    var quantityCell = $(cell).parent().children().get(1);
    var newVal = quantityCell.innerHTML / 1 - 1;
    if (newVal < 0) {
        quantityCell.innerHTML = 0;
    } else {
        quantityCell.innerHTML = newVal;
    }
}

function addSmall(pizza) {
    addToppings(pizza, "1");
}

function addNormal(pizza) {
    addToppings(pizza, "2");
}

function addBig(pizza) {
    addToppings(pizza, "3");
}

function refreshToppingsDialog(pizza) {

    var currentToppings = "" + $("#" + pizza).find(".topping-list").html().replace(/\s /g, '');

    $(".topping-name").each(function (index, entry) {

        var cell = $(entry).parent().children().eq(1);

        if (currentToppings.indexOf(entry.innerHTML) != -1) {
            $(cell).text(1);
        } else {
            $(cell).text(0);
        }
    });
}
function addToppings(pizza, pizzaSize) {

    refreshToppingsDialog(pizza);

    $("#toppingsDialog")
        .data("pizza", pizza)
        .data("pizzaSize", pizzaSize)
        .dialog();
}

function addToCart() {

    var dialog = $("#toppingsDialog");
    var pizza = dialog.data("pizza");
    var pizzaSize = dialog.data("pizzaSize");
    var chosenToppings = [];

    $(dialog).find("tr").each(function (index, entry) {
        var cells = $(entry).find("td");
        var number = $(cells)[1].innerHTML / 1;

        for (var i = 0; i < number; i++) {
            chosenToppings.push($(cells)[0].innerHTML);
        }
    });

    $.ajax({
        type: 'POST',
        url: '/ajax/save_basket_session/',
        dataType: 'json',
        data: {
            'pizza_name': pizza,
            'pizza_size': pizzaSize,
            'toppings': chosenToppings
        },
        success: function (data) {
            $("#cart").find("tbody tr").remove();
            fillCart(data);
        }
    });
}

function toggleCart() {
    $("#cart").toggle();
}

function sizeToText(size) {

    switch (size) {
        case "1":
            return "mała";
        case "2":
            return "średnia";
        case "3":
            return "duża";
    }
}

function fillCart(data) {

    var table = document.getElementById("cart").getElementsByTagName("tbody")[0];
    var price = 0;

    if (data.length > 0) {
        $("#place-order-link").removeClass("disabled");
        $("#clear-cart-button").removeClass("disabled");
    }

    $(data).each(function (index, item) {

        var row = table.insertRow(table.rows.length);
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        var cell3 = row.insertCell(2);

        cell1.innerHTML = item[0];
        cell2.innerHTML = sizeToText(item[1]);
        cell3.innerHTML = parseFloat(item[3]).toFixed(2);

        price += item[3] / 1;
    });

    $("#total-price").text(parseFloat(price).toFixed(2) + " zł");
}

function refreshCart() {

    $.ajax({
        type: 'GET',
        url: '/ajax/get_basket_session/',
        dataType: 'json',
        success: function (data) {
            fillCart(data);
        }
    });
}

function clearCart() {

    $.ajax({
        type: 'GET',
        url: '/ajax/delete_basket_session/',
        success: function () {
            document.getElementById("cart").getElementsByTagName("tbody")[0].innerHTML = "";
            $("#total-price").text("0 zł");
            $("#place-order-link").addClass("disabled");
            $("#clear-cart-button").addClass("disabled");
        }
    });
}

function choosePizzeria(pizzeriaName) {

    $.ajax({
        type: 'POST',
        url: '/ajax/set_pizzeria_session/',
        data: {
            'pizzeria_name': pizzeriaName
        },
        success: function (data) {
            console.log(data);
            location.href = "/pizzeria";
        }
    });
}

function addressSelected() {

    var isAddressChosen = $("#address").val() != '';
    if (isAddressChosen) {
        $("#new-address").hide(300);
        $(".address-field").removeAttr("required");
    } else {
        $("#new-address").show(300);
        $(".address-field").attr("required", true);
    }
}

function changeDelivery() {

    var isTakeout = $("input:checked").val() == "takeout";

    if (isTakeout) {
        $("#address-chooser").hide(300);
        $(".address-field").removeAttr("required");
    } else {
        $("#address-chooser").show(300);
        $(".address-field").attr("required");
    }
}

function startTimer(duration, display) {

    var timer = duration, minutes, seconds;

    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            timer = duration;
        }
    }, 1000);
}