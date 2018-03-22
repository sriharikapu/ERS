from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model,authenticate
from django.contrib.auth.forms import PasswordResetForm,SetPasswordForm
from django.conf import settings

from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    Serializer
)

from rest_framework import serializers, exceptions

from ..models import TokenModel
User = get_user_model()


class TokenSerializer(ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = TokenModel
        fields = ('key',)


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','middle_name','email','date_of_birth',
                    'password','nationality',
                    'address_line_1','address_line_2','address_line_3',
                    'city','state','postal_code','work_address',
                    'user_id')

        extra_kwargs ={
            "password": {"write_only": True }
        }

    def create(self, validated_data):
        user=User.objects.create_user(
            **validated_data
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class UserLoginSerializer(Serializer):
    '''
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]

        extra_kwargs ={
            "password": {"write_only": True }
        }'User',
    '''
    email= serializers.EmailField(required=False,allow_blank=True)
    password=serializers.CharField(style={'input_type': 'password'})

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = authenticate(email=email, password=password)
        else:
            'User',
            msg = ('Must include "email" and "password".')
            raise ValidationError(msg)

        return user

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if email:
            'User',
            user = self._validate_email(email, password)
        else:
            raise ValidationError("Please enter Email and Password")

            # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = ('User account is disabled.')
                raise ValidationError(msg)
        else:
            msg = ('Unable to log in with provided credentials.')
            raise ValidationError(msg)

        attrs['user'] = user
        return attrs


class UserDetailsSerializer(ModelSerializer):
    """'User',
    User model w/o password
    """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'user_id', 'settings')
        read_only_fields = ('user_id', )


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length= 128)
    new_password1 = serializers.CharField(max_length= 128)
    new_password2 =serializers.CharField(max_length= 128)

    set_password_form_class =SetPasswordForm

    def __init__(self,*args,**kwargs):
        self.old_password_field_enabled = getattr(
            settings, 'OLD_PASSWORD_FIELD_ENABLED', False
        )
        self.logout_on_password_change = getattr(
            settings, 'LOGOUT_ON_PASSWORD_CHANGE', False
        )
        super(PasswordChangeSerializer, self).__init__(*args, **kwargs)
        if not self.old_password_field_enabled:
            self.fields.pop('old_password')

        self.request = self.context.get('request')
        self.user = getattr(self.request, 'user', None)

    def validate_old_password(self,value):
        invalid_password_conditions = (
            self.old_password_field_enabled,
            self.user,
            not self.user.check_password(value)
        )

        if all(invalid_password_conditions):
            raise ValidationError('Invalid password')
        return value

    def validate(self, attrs):
        self.set_password_form = self.set_password_form_class(
            user=self.user, data=attrs
        )
        if not self.set_password_form.is_valid():
            raise serializers.ValidationError(self.set_password_form.errors)
        return attrs

    def save(self):
        self.set_password_form.save()
        if not self.logout_on_password_change:
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(self.request, self.user)


class PinChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('security_question_1', 'security_question_2')


class PasswordResetSerializer(serializers.Serializer):
    """
    Serializer for requesting a password reset e-mail.
    """
    email = serializers.EmailField()

    password_reset_form_class = PasswordResetForm

    def get_email_options(self):
        """Override this method to change default e-mail options"""
        return {}

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return value

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)
