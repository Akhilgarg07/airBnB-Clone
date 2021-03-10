from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHERS = "others"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHERS, "Other")
    )

    LANGUAGE_ENGLISH = "english"
    LANGUAGE_HINDI = "hindi"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH,"English"),
        (LANGUAGE_HINDI, "Hindi")
    )

    CURRENCY_USD = "usd"
    CURRENCY_RUP = "rupee"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "USD"),
        (CURRENCY_RUP, "RUPEE")
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15,blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES,max_length=15, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=15,blank=True)
    superhost = models.BooleanField(default=False)