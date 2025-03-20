# forms.py
from django import forms
from .models import Product, Contact, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'price']
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'category', 'price']


class CheckoutForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(max_length=200)
# Include price in the form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order  # Make sure to specify the model here
        fields = ['name', 'email', ]  # Include the necessary fields