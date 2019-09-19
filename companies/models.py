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
        help_text=_("Company"),
        #verbose_name=_("name"),
    )
    address = models.CharField(
        #_('address'),
        default=None,
        max_length=128,
        help_text=_("Physical address"),
        verbose_name=_("address"),
    )
    state = models.CharField(
        _('state'),
        max_length=128,
        default=None,
        null=True,
        help_text=_("State"),
    )
    country = models.CharField(
        _('country'),
        max_length=12,
        default="mx",
        help_text=_("Country"),
    )
    phone = models.CharField(_('phone'), max_length=128)
#    phone = PhoneNumberField(_('phone'), null=False, blank=False, unique=True)
    # slug = AutoSlugField(
    #     populate_from='name',
    #     unique=True,
    #     editable=False
    # )
    # admin = models.ForeignKey(
    #     'accounts.Account',
    #     on_delete=models.CASCADE,
    #     related_name='companies',
    #     help_text=_('Account administrator for this company'),
    #     default=None,
    # )

    class Meta:
        verbose_name = _('Company'),
        verbose_name_plural = _('Companies')

    def __str__(self):
        return f"{self.name}"
