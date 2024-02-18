# flip_detection/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FlipDetection
from .serializers import FlipDetectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
# for swagger api test
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class FlipDetectionAPIView(APIView):
    # for swagger api test
    @swagger_auto_schema(
        request_body=FlipDetectionSerializer,
        manual_parameters=[
            openapi.Parameter(
                'Authorization',
                openapi.IN_HEADER,
                description="Bearer 토큰",
                type=openapi.TYPE_STRING
            )
        ]
    )
    def post(self, request):
        serializer = FlipDetectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)