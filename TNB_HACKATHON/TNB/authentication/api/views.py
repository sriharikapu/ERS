from django.db.models import Q
from django.contrib.auth import get_user_model

from django.contrib.auth import (
    login as django_login,
    logout as django_logout
)
from django.views.decorators.debug import sensitive_post_parameters

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView
)
from authentication.utils import default_create_token

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist, ValidationError

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from authentication.app_settings import (
    LoginSerializer,
    TokenSerializer,
    RegisterSerializer,
    UserDetailsSerializer,
    create_token,
    PasswordChangeSerializer,
    PasswordResetSerializer,
    PinChangeSerializer,
    )

from authentication.models import TokenModel
from static_msg import RETURN_MSG, ERROR_MSG, SUCCESS_MSG
from lib.custom_return import return_msg


User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    model = User
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(GenericAPIView):
    """
       Check the credentials and return the REST Token
       if the credentials are valid and authenticated.
       Calls Django Auth login method to register User ID
       in Django session framework
       Accept the following POST parameters: username, password
       Return the REST Framework Token Object's key.
    """
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    token_model = TokenModel

    def dispatch(self, *args, **kwargs):
        return super(UserLoginAPIView, self).dispatch(*args, **kwargs)

    def process_login(self):
        django_login(self.request, self.user)

    def get_response_serializer(self):
        response_serializer = TokenSerializer
        return response_serializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token=create_token(TokenModel,self.user,self.serializer)

    def get_response(self):
        serializer_class = self.get_response_serializer()
        serializer = serializer_class(
                        instance=self.token,
                        context={'request': self.request})
        return Response(return_msg(RETURN_MSG['SUCCESS'], serializer.data),
                         status= HTTP_200_OK)

    def post(self,request,*args,**kwargs):
        self.request=request
        self.serializer=self.get_serializer(data=self.request.data,
                        context={'request':request})
        self.serializer.is_valid(raise_exception=True)
        self.login()
        return self.get_response()


class UserLogoutAPIView(APIView):
    """
        Calls Django logout method and delete the Token object
        assigned to the current User object.
        Accepts/Returns nothing.
    """

    permission_classes = (AllowAny,)

    def logout(self,request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        django_logout(request)
        return Response(return_msg(RETURN_MSG['SUCCESS'], 
                        SUCCESS_MSG['LOGOUT_SUCCESS']))

    def get(self,request,*args,**kwargs):
        response=self.logout(request)
        return self.finalize_response(request,response,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.logout(request)



class UserDetailsView(APIView):
    """
        Reads and updates UserModel fields
        Accepts GET, PUT, PATCH methods.
        Default accepted fields: username, first_name, last_name
        Default display fields: pk, username, email, first_name, last_name
        Read-only fields: pk, email
        Returns UserModel fields.
    """
    serializer_class = UserDetailsSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        try:
            result = self.serializer_class(
                        self.queryset.get(
                            wallet_id=request._user.wallet_id
                    )).data
            return Response(
                return_msg(RETURN_MSG['SUCCESS'], result), status=200)
        except Exception as e:
            return Response(return_msg(RETURN_MSG['FAIL'], 
                    ERROR_MSG['SERVER_ERROR']), status=400)

    def get_queryset(self):
        """
        Adding this method since it is sometimes called when using
        django-rest-swagger
        https://github.com/Tivix/django-rest-auth/issues/275
        """
        return get_user_model().objects.none()


class PasswordChangeView(GenericAPIView):
    """
        Calls Django Auth SetPasswordForm save method.
        Accepts the following POST parameter
        
        PinChangeSerializers: new_password1, new_password2
        
        Returns the success/fail message.
    """
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def dispatch(self, *args, **kwargs):
        return super(PasswordChangeView, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(return_msg(RETURN_MSG['SUCCESS'], 
                            SUCCESS_MSG['NEW_PASSWORD']))
        except Exception as e:
            return Response(return_msg(RETURN_MSG['FAIL'], str(e)))


class PasswordResetView(GenericAPIView):
    """
        Calls Django Auth PasswordResetForm save method.
        Accepts the following POST parameters: email
        Returns the success/fail message.
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            # Create a serializer with request.data
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save()
            # Return the success message with OK HTTP status
            return Response(return_msg(RETURN_MSG['SUCCESS'], 
                SUCCESS_MSG['RESET_EMAIL_SENT']), status=200)
        except Exception as e:
            return Response(return_msg(RETURN_MSG['FAIL'], 
                ERROR_MSG['SERVER_ERROR']), status=400)

