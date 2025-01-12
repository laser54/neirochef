from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from .views import redoc_view
from users.views import user_login, user_register  # Импортируем напрямую

schema_view = get_schema_view(
    openapi.Info(
        title="Neirochef API",
        default_version='v1',
        description="Документация API для Neirochef",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="your_email@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('api/', include('users.urls')),  # Подключение API-маршрутов
    path('login/', user_login, name='user_login'),  # Прямое подключение логина
    path('register/', user_register, name='user_register'),  # Прямое подключение регистрации
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', redoc_view, name='redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
