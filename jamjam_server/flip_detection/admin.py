# flip_detection/admin.py

from django.contrib import admin

# Django 관리자 페이지에서 FlipDetection모델을 관리할 수 있도록 등록
from .models import FlipDetection

admin.site.register(FlipDetection)