function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken",
                $('input[name="csrfmiddlewaretoken"]').val());
        }
    }
});

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
        }
    });
}

function toggleCart() {
    $("#cart").toggle();
}

function refreshCart() {

    $.ajax({
        type: 'GET',
        url: '/ajax/get_basket_session/',
        dataType: 'json',
        success: function (data) {
            console.log(data);
        }

    });
}

