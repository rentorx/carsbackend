from django.db import models
from commons.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
#from phonenumber_field.modelfields import PhoneNumberField


class Company(TimeStampedModel):
    """
    labeled companies
    """

    name = models.CharField(_('name'), max_length=128)
    address = models.CharField(_('address'), max_length=128)
    phone = models.CharField(_('phone'), max_length=128)
#    phone = PhoneNumberField(_('phone'), null=False, blank=False, unique=True)
    email = models.EmailField(
        _('email'),
        max_length=70,
        null=True,
        blank=True,
        unique=True,
    )

    slug = AutoSlugField(
        populate_from='name',
        unique=True,
        editable=False
    )
    admins = models.ManyToManyField(
        'accounts.Account',
        related_name='companies',
        blank=True
    )

    class Meta:
        verbose_name = _('company'),
        verbose_name_plural = _('companies')

    def __str__(self):
        return f"{self.name}"
