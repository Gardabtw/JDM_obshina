from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
import json
from cars.models import Car
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Сохраняем нового пользователя
            user = form.save(commit=False)  # Мы сохраняем объект, но не подтверждаем его сохранение в базе данных
            user.set_password(form.cleaned_data['password1'])  # Устанавливаем пароль в зашифрованном виде
            user.save()  # Сохраняем пользователя в базе данных

            messages.success(request, 'Вы успешно зарегистрировались!')
            login(request, user)  # Входим в систему сразу после регистрации

            return redirect('home')  # Перенаправляем на главную страницу или другую страницу
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})



def register_car(request):
    if request.method == 'POST':
        form = CarRegistrationForm(request.POST)
        if form.is_valid():
            car = form.save()  # Сохраняем машину в базе данных
            messages.success(request, 'Машина успешно зарегистрирована!')
            return redirect('car_details', car_id=car.id)  # Перенаправляем на страницу с деталями машины
    else:
        form = CarRegistrationForm()

    return render(request, 'registration/register_car.html', {'form': form})




def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Проверяем данные пользователя
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Вы успешно вошли!')
            return redirect('home')  # Перенаправляем на главную страницу
        else:
            messages.error(request, 'Неверные данные для входа.')

    return render(request, 'registration/login_user.html')