from .models import Orders, Products, Customers
from django.forms import ModelForm, TextInput, Select, DateInput, NumberInput, EmailInput


class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ["order_number", "order_date", "prod", "cust", "quantity", "price"]
        widgets = {
            "order_number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер',
                'required': True
            }),
            "order_date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата заказа',
                'required': True
            }),
            "prod": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Товар',
                'required': True
            }),
            "cust": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Клиент',
                'required': True
            }),
            "quantity": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество',
                'required': True
            }),
            "price": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Цена',
                'required': True
            })
        }


class ProdForm(ModelForm):
    class Meta:
        model = Products
        fields = ["title"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование',
                'required': True
            }),
        }


class CustForm(ModelForm):
    class Meta:
        model = Customers
        fields = ["name", "surname", "phone", "email"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'required': True
            }),
            "surname": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия',
                'required': True
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон',
                'required': True
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта',
                'required': True
            }),
        }
