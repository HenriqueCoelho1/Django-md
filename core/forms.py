from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    email = forms.EmailField(label="Email", max_length=200)
    subject = forms.CharField(label="Subject", max_length=120)
    message = forms.CharField(label="Message", widget=forms.Textarea())
