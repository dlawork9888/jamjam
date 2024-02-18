# flip_detection/serializers.py

from rest_framework import serializers
from .models import FlipDetection

class FlipDetectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlipDetection
        fields = ['flip_score', 'flip_time', 'user_id']