from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date
from dateutil.relativedelta import relativedelta  # 날짜 계산 목적!

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, name, nickname, email, phone_num, child_name, child_birth, child_gender, password=None, **extra_fields):
        if not name:
            raise ValueError('The Name field must not be empty')
        if not nickname:
            raise ValueError('The Nickname field must not be empty')
        if not email:
            raise ValueError('The Email field must not be empty')
        if not phone_num:
            raise ValueError('The Phone Number field must not be empty')
        if not child_name:
            raise ValueError('The Child Name field must not be empty')
        if not child_birth:
            raise ValueError('The Child Birth field must not be empty')
        if not child_gender:
            raise ValueError('The Child Gender field must not be empty')
        
        user = self.model(
            name=name,
            nickname=nickname,
            email=self.normalize_email(email),
            phone_num=phone_num,
            child_name=child_name,
            child_birth=child_birth,
            child_gender=child_gender,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, nickname, name, phone_num, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(
            email=email,
            password=password,
            nickname=nickname,
            name=name,
            phone_num=phone_num,
            **extra_fields
        )

class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    nickname = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, unique=True)
    phone_num = models.CharField(max_length=20, blank=False, unique=True)
    child_name = models.CharField(max_length=100, blank=False)
    child_birth = models.DateField(blank=False)
    child_gender = models.CharField(
        max_length=1,
        choices=(('M', '남자'), ('F', '여자')),
        default='M',
    )
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # 관리자 페이지 접근 권한
    is_superuser = models.BooleanField(default=False)  # 전체 관리자 권한

    objects = UserManager()

    USERNAME_FIELD = 'nickname'
    REQUIRED_FIELDS = ['email', 'name', 'phone_num', 'child_name', 'child_birth', 'child_gender']
    
    
    def __str__(self):
        return self.nickname

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
