# flip_detection/urls.py
# settings.py에 추가됨

from django.urls import path
from .views import FlipDetectionAPIView

urlpatterns = [
    path('post/', FlipDetectionAPIView.as_view(), name='create_flip_detection'),
]
