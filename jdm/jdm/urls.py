from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from register import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('register-car/', views.register_car, name='register_car'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

