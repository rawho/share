from django.shortcuts import render, redirect
from .forms import CreateUserForm
# Create your views here.

def index(request):
    form = CreateUserForm(request.POST)
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'library/index.html', {
        'form' : form
    })