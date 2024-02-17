from .models import User
from rest_framework import serializers
from datetime import date
from dateutil.relativedelta import relativedelta

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    age_in_months = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['nickname', 'name', 'email', 'phone_num', 'child_name', 'child_birth', 'child_gender', 'password', 'age_in_months']

    def get_age_in_months(self, obj):
        current_date = date.today()
        birth_date = obj.child_birth
        age_in_months = relativedelta(current_date, birth_date).years * 12 + relativedelta(current_date, birth_date).months
        return age_in_months

    def create(self, validated_data):
        # User.objects.create_user를 사용하여 사용자 생성
        user = User.objects.create_user(
            nickname=validated_data['nickname'],
            name=validated_data['name'],
            email=validated_data['email'],
            phone_num=validated_data.get('phone_num', ''),
            child_name=validated_data.get('child_name', ''),
            child_birth=validated_data.get('child_birth'),  # 날짜 변환 로직은 create_user 내부에 구현되어 있어야 합니다.
            child_gender=validated_data.get('child_gender', 'M'),  # 기본값 'M' 설정
            password=validated_data['password']
        )
        return user

class UserInfoSerializer(serializers.ModelSerializer):
    age_in_months = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['nickname', 'name', 'email', 'phone_num', 'child_name', 'child_birth', 'child_gender', 'age_in_months']

    def get_age_in_months(self, obj):
        current_date = date.today()
        birth_date = obj.child_birth
        age_in_months = relativedelta(current_date, birth_date).years * 12 + relativedelta(current_date, birth_date).months
        return age_in_months
