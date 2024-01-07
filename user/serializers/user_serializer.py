from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from user.models import *
from allauth.account import app_settings as allauth_settings
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import filter_users_by_email

from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    password2 = None

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            # Check if the email is already being used
            users = filter_users_by_email(email)
            if len(users) > 0:
                raise serializers.ValidationError(
                    "A user is already registered with this email address."
                )
        return email

    def validate(self, data):
        return data


class CustomLoginSerializer(LoginSerializer):
    username = None  # Remove the default username field

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Remove the password field from the response
        data.pop('password', None)
        return data


class UserSerializer(RegisterSerializer):
    password2 = None

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            # Check if the email is already being used
            users = filter_users_by_email(email)
            if len(users) > 0:
                raise serializers.ValidationError(
                    "A user is already registered with this email address."
                )
        return email

    def validate(self, data):
        return data
