from django import forms
from django.core.exceptions import ValidationError
from .models import Product, Consumer


class AddProduct(forms.Form):

    id_product = forms.IntegerField(label='Id product')
    product_name = forms.CharField(max_length=50, label='Product name')
    description = forms.CharField(widget=forms.Textarea, label='Product description')
    image = forms.ImageField(label='Product image')
    matrix_type = forms.CharField(max_length=50, label='Matrix type')
    ligand = forms.CharField(max_length=50, label='Ligand')
    economic_stage = forms.ChoiceField(choices=Product.economic_stages, label='Economic stage')
    registration = forms.CharField(max_length=50, label='Registration')
    price = forms.DecimalField(max_digits=8, decimal_places=2, label='Price')
    
    def clean_product_name(self):
        t = self.cleaned_data['id_product']
        if len(t) != 5:
            raise ValidationError("Incorrect id product!")

        return t

class AddConsumer(forms.Form):

    consumer_name = forms.CharField(max_length=100, label='Сonsumer name')
    adress = forms.CharField(max_length=200, label='Adress')
    phone_number = forms.IntegerField(label='Phone number')
    postcode = forms.IntegerField(label='Postcode')
    site = forms.URLField(max_length=100, label='Site')
    transportation = forms.ChoiceField(choices=Consumer.transportations, label='Transportation')
