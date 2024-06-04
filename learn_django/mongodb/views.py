from django.shortcuts import render, redirect
from .db import get_products, get_info_product, add_product, add_field, delete_field, get_product_name, delete_product


def home_page(request):
    products = get_products()
    return render(request, "mongodb/home_page.html", {"products": products})


def add_product_view(request):
    if request.method == "GET":
        return render(request, "mongodb/add_product.html")
    else:
        data = request.POST
        if 'Name' in data and 'Amount' in data:
            res = {key: value for key, value in data.items() if key != "csrfmiddlewaretoken"}
            add_product(res)
        return redirect("/")


def product_info(request, product_id):
    product_name, product_fields, product_values = get_info_product(product_id)
    data = {
        "product_name": product_name,
        "product": zip(product_fields, product_values),
        "product_id": product_id
    }
    return render(request, "mongodb/see_product.html", data)


def field_edit(request, product_id, field_name):
    if request.method == "GET":
        data = {
            "field_name": field_name,
            'product_name': get_product_name(product_id)
        }
        return render(request, "mongodb/change_field.html", data)
    else:
        value = request.POST['field_value']
        if request.POST['button_clicked'] == "delete":
            if field_name == "Name" or field_name == "Amount" or field_name == "_id":
                return redirect(product_info, product_id)
            delete_field(product_id, field_name)
        else:
            add_field(product_id, field_name, value)

        return redirect(product_info, product_id)


def field_add(request, product_id):
    if request.method == "GET":
        return render(request, "mongodb/add_field.html", {'product_name': get_product_name(product_id)})
    else:
        field_name = request.POST['field_name']
        if field_name == "Name" or field_name == "Amount" or field_name == "_id":
            return redirect(product_info, product_id)
        value = request.POST['field_value']
        add_field(product_id, field_name, value)

        return redirect(product_info, product_id)


def delete_product_view(request, product_id):
    delete_product(product_id)
    return redirect("/")