from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class ProtectedEndpointView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Пример защищенного эндпоинта",
        responses={200: openapi.Response('Доступ разрешен!', schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'message': openapi.Schema(type=openapi.TYPE_STRING, description='Сообщение'),
            },
        ))},
    )
    def get(self, request):
        return Response({"message": "Доступ разрешен!"})
