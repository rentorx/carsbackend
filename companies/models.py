from django.db import models
from commons.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
#from phonenumber_field.modelfields import PhoneNumberField


class Company(TimeStampedModel):
    """
    labeled companies
    """

    name = models.CharField(
        _('name'),
        max_length=128,
        help_text="Compani's name",
    )
    address = models.CharField(
        _('address'),
        default=None,
        max_length=128,
        help_text="physical address",
    )
    state = models.CharField(
        _('state'),
        max_length=128,
        default=None,
        null=True,
        help_text="State",
    )
    country = models.CharField(
        _('country'),
        max_length=12,
        default="mx",
        null=True,
        help_text="country",
    )
    phone = models.CharField(_('phone'), max_length=128)
#    phone = PhoneNumberField(_('phone'), null=False, blank=False, unique=True)
    slug = AutoSlugField(
        populate_from='name',
        unique=True,
        editable=False
    )
    admins = models.ForeignKey(
        'accounts.Account',
        related_name='admins',
        on_delete=models.CASCADE,
        default=None
    )

    class Meta:
        verbose_name = _('company'),
        verbose_name_plural = _('companies')

    def __str__(self):
        return f"{self.name}"
