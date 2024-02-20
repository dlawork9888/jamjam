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
        # API 상세 설명
        operation_description = 'Flip Detection Record Post 요청\n***주의! => Authorization에 토큰 입력 시 꼭 "Bearer {token}"형태로 넣어주세요!',
        # Request Body Parameter <= Serializer
        request_body=FlipDetectionSerializer,
        # Bearer Token 입력
        ### !!! 꼭 토큰 앞에 {Bearer + ' '}를 붙여야 함 !!!
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