from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm


def index(request):
    return render(request, "index.html")


def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method) == "POST":
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            messages.success(request, "Email was send with success")
            form = ContactForm()
        else:
            messages.error(request, "Error to send email")

    context = {"form": form}
    return render(request, "contact.html", context)


def product(request):
    return render(request, "product.html")
