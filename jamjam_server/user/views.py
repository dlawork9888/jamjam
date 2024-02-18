from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from .serializers import UserSerializer, LoginSerializer
# for swagger api test
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request): 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# swagger에서 auth token 얻기 위해 살짝 바꿨음(dlawork9888)
@swagger_auto_schema(method='post', request_body=LoginSerializer)
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        nickname = serializer.validated_data.get('nickname')
        password = serializer.validated_data.get('password')

        user = authenticate(request, username=nickname, password=password)
        if user is None:
            return Response({'message': '아이디 또는 비밀번호가 일치하지 않습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

        # 토큰 생성 및 최종 로그인 시간 업데이트
        refresh = RefreshToken.for_user(user)
        update_last_login(None, user)

        return Response({
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token)
        }, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)