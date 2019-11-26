from django.shortcuts import render
from .forms import projectForm
from .models import project

# Create your views here.
def projectCreate_view(request):
    form = projectForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        project.objects.create(**form.cleaned_data)
    template_name = "form.html"
    context = {
        'title': 'from projectCreate_view',
        'form': form
    }
    return render(request, "form.html", context)
