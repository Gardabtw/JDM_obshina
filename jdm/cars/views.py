from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.decorators import login_required
from .models import Car

class CarFilterForm(forms.Form):
    name = forms.CharField(required=False)
    min_price = forms.DecimalField(required=False)
    max_price = forms.DecimalField(required=False)

def buy_car_list(request):
    cars = Car.objects.filter(available=True)
    filter_form = CarFilterForm(request.GET)

    if filter_form.is_valid():
        if filter_form.cleaned_data['name']:
            cars = cars.filter(name__icontains=filter_form.cleaned_data['name'])
        if filter_form.cleaned_data['min_price']:
            cars = cars.filter(price__gte=filter_form.cleaned_data['min_price'])
        if filter_form.cleaned_data['max_price']:
            cars = cars.filter(price__lte=filter_form.cleaned_data['max_price'])

    return render(request, 'cars/buyer.html', {'cars': cars, 'filter_form': filter_form})



def home(request):
    return render(request, 'main/web.html')

@login_required(login_url='/register/')
def sell_car(request):
    cars = request.user.cars.all()  # Получаем все машины текущего пользователя
    return render(request, 'cars/seller.html', {'cars': cars})

def buy_car_list(request):
    cars = Car.objects.filter(available=True)  # Получаем все доступные для покупки автомобили
    return render(request, 'cars/buyer.html', {'cars': cars})

@login_required(login_url='/register/')
def car_detail(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        raise Http404("Машина не найдена")
    return render(request, 'cars/car_detail.html', {'car': car})