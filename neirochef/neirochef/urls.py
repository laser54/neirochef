from django.urls import path, include

urlpatterns = [
    path('api/auth/', include('djoser.urls')),         # Djoser эндпоинты
    path('api/auth/', include('djoser.urls.jwt')),    # JWT эндпоинты
    path('api/', include('users.urls')),              # Маршруты приложения users
]

