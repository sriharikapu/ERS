from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import password_reset_confirm
from .views import (
    UserCreateAPIView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserDetailsView,
    PasswordChangeView,
    PasswordResetView,
)

urlpatterns = [
    url(r'^register/$',UserCreateAPIView.as_view(),name='register'),
    url(r'^login/$',UserLoginAPIView.as_view(),name='login'),
    url(r'^logout/$', UserLogoutAPIView.as_view(), name='logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(),name='password_change'),
    url(r'^password/reset/$', PasswordResetView.as_view(),name='password_reset'),
]

