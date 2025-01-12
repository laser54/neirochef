from django.urls import path
from .views import ProtectedEndpointView, user_login, user_register

urlpatterns = [
    # Защищенный эндпоинт
    path('protected-endpoint/', ProtectedEndpointView.as_view(), name='protected-endpoint'),

    # Логин
    path('login/', user_login, name='user_login'),

    # Регистрация
    path('register/', user_register, name='user_register'),
]
