from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token as DefaultTokenModel
from django.core.exceptions import ObjectDoesNotExist
from django_countries.fields import CountryField

TokenModel = DefaultTokenModel


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, is_staff=False, is_admin=False, is_active=True, **kwargs):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have an email address")
        user_obj = self.model(
            email=self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.is_active = is_active
        user_obj.first_name = kwargs['first_name']
        user_obj.last_name = kwargs['last_name']
        user_obj.middle_name = kwargs['middle_name']
        user_obj.nationality = kwargs['nationality']
        user_obj.date_of_birth = kwargs['date_of_birth']
        user_obj.address_line_1 = kwargs['address_line_1']
        user_obj.address_line_2 = kwargs['address_line_2']
        user_obj.address_line_3 = kwargs['address_line_3']
        user_obj.city = kwargs['city']
        user_obj.state = kwargs['state']
        user_obj.postal_code = kwargs['postal_code']
        user_obj.work_address = kwargs['work_address']
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email,
            password=password,
            is_staff=True, **kwargs
        )
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True,
            **kwargs
        )
        return user


# Create your models here.
class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=200, null=True)
    tnb_holding = models.IntegerField(null=False, default=0)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    address_line_3 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=15, blank=True, null=True)
    work_address = models.CharField(max_length=150, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name','last_name','middle_name','date_of_birth',
                       'nationality','address_line_1','address_line_2','address_line_3',
                       'city','state','postal_code','work_address'
                       ]

    objects = UserManager()

    def __str__(self):
        return self.wallet_id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_short_name(self):
        return self.first_name