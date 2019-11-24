from django.shortcuts import render
from tracker.form import projectForm

# Create your views here.
def projectCreate_view(request):
    form = projectForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    template_name = "forms.html"
    context = {
        'form': form
    }
    return render(request, template_name, context)


