from django.shortcuts import render

from tracker.forms import projectModelForm, accountModelForm, recordModelForm, commentModelForm
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


# Create your views here.
def accountCreate_view(request):
    form = accountModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = projectModelForm()
    template_name = 'createAccount_Form.html'
    context = {
        "title": "Account create form",
        "action": "/createAccount",
        'form': form
    }
    return render(request, template_name, context)


# Create your views here.
def projectCreate_view(request):
    form = projectModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = projectModelForm()
    template_name = 'createProject_Form.html'
    context = {
        "title": "Project create form",
        "action": "/createProject",
        'form': form
    }
    return render(request, template_name, context)

# Create your views here.
def commentCreate_view(request):
    form = commentModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = projectModelForm()
    template_name = 'createComment_Form.html'
    context = {
        "title": "Comment create form",
        "action": "/createComment",
        'form': form
    }
    return render(request, template_name, context)


# Create your views here.
def recordCreate_view(request):
    form = recordModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = projectModelForm()
    template_name = 'createRecord_Form.html'
    context = {
        "title": "Record create form",
        "action": "/createRecord",
        'form': form
    }
    return render(request, template_name, context)

