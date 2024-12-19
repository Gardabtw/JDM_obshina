from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sell/', views.sell_car, name='seller'),
    path('buy/', views.buy_car_list, name='buyer'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
]