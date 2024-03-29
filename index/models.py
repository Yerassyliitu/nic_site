import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models


# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         """ Создает и возвращает пользователя с имэйлом, паролем и именем. """
#         if username is None:
#             raise TypeError('Users must have a username.')
#
#         if email is None:
#             raise TypeError('Users must have an email address.')
#
#         user = self.model(username=username, email=self.normalize_email(email))
#         user.set_password(password)
#         user.save()
#
#         return user
#
#     def create_superuser(self, username, email, password):
#         """ Создает и возввращет пользователя с привилегиями суперадмина. """
#         if password is None:
#             raise TypeError('Superusers must have a password.')
#
#         user = self.create_user(username, email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save()
#
#         return user
#
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(db_index=True, max_length=255, unique=True)
#     email = models.EmailField(db_index=True, unique=True)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.email
#
#     @property
#     def token(self):
#         return self._generate_jwt_token()
#
#     def get_full_name(self):
#         return self.username
#
#
#     def _generate_jwt_token(self):
#         dt = datetime.now() + timedelta(days=1)
#
#         token = jwt.encode({
#             'id': self.pk,
#             'exp': int(dt.strftime('%s'))
#         }, settings.SECRET_KEY, algorithm='HS256')
#
#         return token.decode('utf-8')


class Application(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    letter = models.FileField(null=True, blank=True)
    division = models.ForeignKey('Division', on_delete=models.CASCADE)
    portfolio_link = models.TextField()
    university = models.ForeignKey('University', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=255, default="unchecked")  # accepted, rejected


    def __str__(self):
        return self.firstname + " " + self.lastname


class Division(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class University(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title