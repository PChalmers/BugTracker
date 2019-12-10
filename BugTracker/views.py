from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from tracker.forms import projectModelForm, accountModelForm, recordModelForm, commentModelForm, loginForm
from .form import ContactForm


def home_page(request):
    return render(request, "mainTable.html")


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
        form = accountModelForm()
    template_name = 'createAccount_Form.html'
    context = {
        "title": "Account create form",
        "action": "/createAccount",
        'form': form
    }
    return render(request, template_name, context)

# Create your views here.
@staff_member_required
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
@login_required
def commentCreate_view(request):
    form = commentModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = commentModelForm()
    template_name = 'createComment_Form.html'
    context = {
        "title": "Comment create form",
        "action": "/createComment",
        'form': form
    }
    return render(request, template_name, context)


# Create your views here.
@login_required
def recordCreate_view(request):
    form = recordModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = recordModelForm()
    template_name = 'createRecord_Form.html'
    context = {
        "title": "Record create form",
        "action": "/createRecord",
        'form': form
    }
    return render(request, template_name, context)


def loginToAccount(request):
    form = loginForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            ...
        else:
            # Return an 'invalid login' error message.
            form = loginForm()

    template_name = 'login_Form.html'
    context = {
        "title": "Log in to continue",
        "action": "/login",
        'form': form
    }
    return render(request, template_name, context)