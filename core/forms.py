from django import forms
from django.core.mail.message import EmailMessage

from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    subject_field = forms.CharField(label="Subject", max_length=120)
    message = forms.CharField(label="Message", widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data["name"]
        email = self.cleaned_data["email"]
        subject_field = self.cleaned_data["subject_field"]
        message = self.cleaned_data["message"]

        context = f"Name: {name}, email: {email}, subject :{subject_field}, message: {message}"

        mail = EmailMessage(
            subject=subject_field,
            body=context,
            from_email="my_mail@outlook.com",
            to=["my_mail@outlook.com"],
            headers={"Reply-To": email},
        )

        mail.send()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock", "image"]
