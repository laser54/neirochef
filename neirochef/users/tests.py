from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

User = get_user_model()

class UserAuthTests(APITestCase):
    def setUp(self):
        # Данные для тестов
        self.register_url = '/api/auth/users/'  # URL регистрации
        self.login_url = '/api/auth/jwt/create/'  # URL для получения токенов
        self.refresh_url = '/api/auth/jwt/refresh/'  # URL для обновления токенов
        self.protected_url = '/api/protected-endpoint/'  # Пример защищенного маршрута

        self.user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "ComplexPassword!123",
            "re_password": "ComplexPassword!123",
        }

    def test_user_registration(self):
        """Тест успешной регистрации пользователя"""
        response = self.client.post(self.register_url, self.user_data)
        print("Response data:", response.data)  # Вывод данных ответа
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', response.data)
        self.assertIn('username', response.data)

    def test_user_login(self):
        """Тест успешного логина через JWT"""
        # Сначала регистрируем пользователя
        User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )

        # Выполняем логин
        response = self.client.post(self.login_url, {
            "username": self.user_data['username'],
            "password": self.user_data['password'],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_refresh(self):
        """Тест успешного обновления токена"""
        # Создаем пользователя и получаем токены
        user = User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        response = self.client.post(self.login_url, {
            "username": self.user_data['username'],
            "password": self.user_data['password'],
        })
        refresh_token = response.data['refresh']

        # Обновляем токен
        refresh_response = self.client.post(self.refresh_url, {
            "refresh": refresh_token
        })
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn('access', refresh_response.data)

    def test_access_protected_route(self):
        """Тест доступа к защищенному маршруту с токеном"""
        # Создаем пользователя и получаем токен
        user = User.objects.create_user(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password=self.user_data['password']
        )
        response = self.client.post(self.login_url, {
            "username": self.user_data['username'],
            "password": self.user_data['password'],
        })
        access_token = response.data['access']

        # Пытаемся получить доступ к защищенному маршруту
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
        protected_response = self.client.get(self.protected_url)
        self.assertEqual(protected_response.status_code, status.HTTP_200_OK)
        self.assertIn('message', protected_response.data)

    def test_invalid_token_access(self):
        """Тест доступа к защищенному маршруту с некорректным токеном"""
        self.client.credentials(HTTP_AUTHORIZATION='Bearer invalid_token')
        response = self.client.get(self.protected_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn('detail', response.data)
