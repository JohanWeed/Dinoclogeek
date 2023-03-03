from django.shortcuts import render, redirect
from .models import Contact, Code_Phone_Country
from .forms import CreateNewContact

# Create your views here.

def error_404_view(request, exception):
    return render (request, '404.html')

def Home(request):
    return render(request, 'Home.html')


def WebDesign(request):
    return render(request, 'Servicios/web-design.html')


def SEO(request):
    return render(request, 'Servicios/seo.html')


def FAQ(request):
    return render(request, 'faq.html')


def Contacto(request):
    if request.method == 'GET':
        form = CreateNewContact()
    else:
        form = CreateNewContact(request.POST)
        if form.is_valid():
            prefix_id = form.cleaned_data.get('prefix')
            code_phone = Code_Phone_Country.objects.get(id=prefix_id).code_phone
            name = form.cleaned_data.get('name')
            phone = f"{code_phone} {form.cleaned_data.get('phone')}"
            email = form.cleaned_data.get('email')
            Contact.objects.create(name=name, phone=phone, email=email)
            return redirect('contacto')
    return render(request, 'contacto.html', {'form': form})
