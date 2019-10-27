from django.shortcuts import render
from .form import regForm
from .models import userDetails

# Create your views here.

def getUser(request):
    form = regForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = regForm()

    return render(request, 'register.html', {'myform' : form})
