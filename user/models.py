from django.db import models
from django.contrib.auth.models import AbstractUser
from e_commerce.models import AbstractBaseModel


class User(AbstractUser, AbstractBaseModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
