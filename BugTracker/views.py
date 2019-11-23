from django.http import HttpResponse
from django.shortcuts import render

from .form import ContactForm

def home_page(request):
    return render(request, "main.html")

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "title": "Contact us...",
        "form": form
    }
    return render(request, "contactForm.html", context)