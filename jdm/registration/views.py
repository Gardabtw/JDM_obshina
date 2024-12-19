from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # после успешной регистрации редирект на страницу входа
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})