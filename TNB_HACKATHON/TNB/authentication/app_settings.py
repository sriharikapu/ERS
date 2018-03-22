from django.conf import settings
from authentication.api.serializers import (TokenSerializer as DefaultTokenSerializer,
                                            UserLoginSerializer as DefaultUserLoginSerializer,
                                            UserCreateSerializer as DefaultUserCreateSerializer,
                                            UserDetailsSerializer as DefaultUserDetailsSerializer,
                                            PasswordChangeSerializer as DefaultPasswordChangeSerializer,
                                            PasswordResetSerializer as DefaultPasswordResetSerializer,
                                            PinChangeSerializer as DefaultPinChangeSerializer)

from authentication.utils import default_create_token,import_callable

create_token = import_callable(getattr(settings, 'REST_AUTH_TOKEN_CREATOR', default_create_token))

serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})

TokenSerializer = import_callable(
    serializers.get('TOKEN_SERIALIZER', DefaultTokenSerializer))



LoginSerializer = import_callable(
    serializers.get('LOGIN_SERIALIZER', DefaultUserLoginSerializer)
)

RegisterSerializer = import_callable(
    serializers.get('REGISTER_SERIALIZER', DefaultUserCreateSerializer)
)

UserDetailsSerializer = import_callable(
    serializers.get('USERDETAILS_SERIALIZER', DefaultUserDetailsSerializer)
)

PasswordChangeSerializer = import_callable(
    serializers.get('PASSWORD_CHANGE_SERIALIZER', DefaultPasswordChangeSerializer)
)

PinChangeSerializer = import_callable(
    serializers.get('PIN_CHANGE_SERIALIZER', DefaultPinChangeSerializer)
)

PasswordResetSerializer = import_callable(
    serializers.get('PASSWORD_RESET_SERIALIZER', DefaultPasswordResetSerializer)
)
