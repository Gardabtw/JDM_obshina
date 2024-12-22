from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
import json
from .models import Car

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # после успешной регистрации редирект на страницу входа
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})



    @csrf_exempt
def register_car(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            car_make = data.get('car_make')
            car_model = data.get('car_model')
            car_year = data.get('car_year')
            car_owner = data.get('car_owner')

            if not all([car_make, car_model, car_year, car_owner]):
                return JsonResponse({'error': 'Все поля обязательны'}, status=400)

            car = Car.objects.create(
                car_make=car_make,
                car_model=car_model,
                car_year=car_year,
                car_owner=car_owner
            )
            return JsonResponse({'message': 'Автомобиль зарегистрирован', 'car': {
                'car_make': car.car_make,
                'car_model': car.car_model,
                'car_year': car.car_year,
                'car_owner': car.car_owner
            }}, status=201)
        except ValidationError as e:
            return JsonResponse({'error': str(e)}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Ошибка сервера: ' + str(e)}, status=500)
    return JsonResponse({'error': 'Только POST-запросы разрешены'}, status=405)



def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Получаем пользователя из формы
            user = form.get_user()
            login(request, user)  # Выполняем вход пользователя
            return redirect('home')  # Редирект на домашнюю страницу
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})