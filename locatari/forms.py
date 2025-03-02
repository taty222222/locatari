from django import forms
from .models import Apartament, Reclamatii, Aviz, FacturiIntretinere, Locatari
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Payment
from .models import WaterMeterReading


class WaterMeterReadingForm(forms.ModelForm):
    class Meta:
        model = WaterMeterReading
        fields = [ 'hot_water_index', 'cold_water_index']
        widgets = {


            'hot_water_index': forms.NumberInput(attrs={'class': 'form-input'}),
            'cold_water_index': forms.NumberInput(attrs={'class': 'form-input'}),
        }






DEFAULT_WIDGET_ATTRS = {
    'class': 'w-full py-4 px-6 bg-white text-black rounded-lg'
}


class AvizForm(forms.ModelForm):
    class Meta:
        model = Aviz
        fields = ['titlu', 'continut']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        **DEFAULT_WIDGET_ATTRS
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        **DEFAULT_WIDGET_ATTRS
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        **DEFAULT_WIDGET_ATTRS
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your first name',
        **DEFAULT_WIDGET_ATTRS
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your last name',
        **DEFAULT_WIDGET_ATTRS
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        **DEFAULT_WIDGET_ATTRS
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        **DEFAULT_WIDGET_ATTRS
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        **DEFAULT_WIDGET_ATTRS
    }))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            User.objects.create(user=user, apartament=self.cleaned_data['apartament'])
        return user

class LocatariForm(forms.ModelForm):
    class Meta:
        model = Locatari
        fields = ['apartament']



class ApartamentForm(forms.ModelForm):
    class Meta:
        model = Apartament
        fields = ['numar', 'scara']


class ReclamatiiForm(forms.ModelForm):
    class Meta:
        model = Reclamatii
        fields = ['category', 'titlu', 'description']


class FacturaForm(forms.ModelForm):
    class Meta:
        model = FacturiIntretinere
        fields = ['luna', 'contor_valoare', 'suma_plata', 'pdf_factura', 'achitata', ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['index', 'amount', 'payment_date', 'is_paid']
