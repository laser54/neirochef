from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Кастомная модель пользователя (на основе стандартной)."""
    email = models.EmailField(unique=True)  # Уникальный email

