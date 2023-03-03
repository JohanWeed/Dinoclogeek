from django import forms
from .models import Code_Phone_Country
 
class CreateNewContact(forms.Form):

    name = forms.CharField(label='Nombre Completo', max_length=100)
    PREFIX_CHOICES = Code_Phone_Country.objects.values_list('id', 'code_phone')
    prefix = forms.ChoiceField(
        label='Prefijo',
        initial='157',
        choices=PREFIX_CHOICES,
    )
    phone = forms.CharField(label='Número Télefonico', max_length=20)
    email = forms.EmailField(label='E-mail', max_length=50) 
    message = forms.CharField(
        label='Mensaje',
        max_length=300,
        widget=forms.Textarea(attrs={'rows':4})
    )   