from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm, ProductModelForm


def index(request):
    return render(request, "index.html")


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            form.send_mail()

            messages.success(request, "Email was send with success")
            form = ContactForm()
        else:
            messages.error(request, "Error to send email")

    context = {"form": form}
    return render(request, "contact.html", context)


def product(request):
    if str(request.method) == "POST":
        form = ProductModelForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            print(f"Name: {prod.name}")
            print(f"Price: {prod.price}")
            print(f"Stock: {prod.stock}")
            print(f"Image: {prod.image}")

            messages.success(request, "Product Save with Success")
            form = ProductModelForm()
        else:
            messages.error(request, "Error in save product")
    else:
        form = ProductModelForm()

    context = {"form": form}
    return render(request, "product.html", context)
