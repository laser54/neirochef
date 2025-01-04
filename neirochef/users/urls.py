from django.urls import path
from .views import ProtectedEndpointView

urlpatterns = [
    path('protected-endpoint/', ProtectedEndpointView.as_view(), name='protected-endpoint'),
]
