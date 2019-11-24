from django.http import HttpResponse
from django.shortcuts import render
from .form import ContactForm
from tracker.views import projectForm

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


# Create your views here.
def projectCreate_view(request):
    form = projectForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    template_name = 'forms.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)
