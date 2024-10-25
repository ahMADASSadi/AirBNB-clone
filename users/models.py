from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'
    GENDER_CHOICES = [
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
        (GENDER_OTHER, _('Other')),
    ]

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_PERSIAN = 'fa'
    LANGUAGE_CHOICES = [
        (LANGUAGE_ENGLISH, _('English')),
        (LANGUAGE_PERSIAN, _('Persian')),
    ]
    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"
    CURRENCY_IRR = "irr"

    CURRENCY_CHOICES = [
        (CURRENCY_USD, _("USD")),
        (CURRENCY_KRW, _("KRW")),
        (CURRENCY_IRR, _("IRR")),
    ]

    avatar = models.ImageField(verbose_name=_('Avatar'),
                               upload_to='userprofile/avatar-images/', blank=True)
    gender = models.CharField(verbose_name=_(
        'Gender'), max_length=10,   choices=GENDER_CHOICES, blank=True)
    bio = models.TextField(verbose_name=_('Bio'), blank=True, null=True)
    language = models.CharField(
        max_length=10, choices=LANGUAGE_CHOICES, verbose_name=_('Language'))
    birth_date = models.DateField(
        blank=True, verbose_name=_('Birth Date'), null=True)
    superhost = models.BooleanField(default=False, verbose_name=_('SuperHost'))

    currency = models.CharField(
        max_length=5, choices=CURRENCY_CHOICES, verbose_name=_("Currency"), default=CURRENCY_USD)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
