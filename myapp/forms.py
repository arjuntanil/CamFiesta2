from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Review

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Product

from django import forms
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=15, required=False, help_text="Enter your phone number.")
    address = forms.CharField(widget=forms.Textarea, required=False, help_text="Enter your address.")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True, help_text="Enter your phone number.")
    address = forms.CharField(widget=forms.Textarea, required=True, help_text="Enter your address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
    rating = forms.ChoiceField(choices=Review.RATING_CHOICES)

    def __init__(self, *args, **kwargs):
        product = kwargs.get('initial', {}).get('product')
        if product:
            self.fields['product'] = forms.ModelChoiceField(queryset=Product.objects.filter(id=product.id), widget=forms.HiddenInput(), initial=product)
        super().__init__(*args, **kwargs)

