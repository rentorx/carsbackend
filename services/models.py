from django.db import models
from commons.models import TimeStampedModel
from djmoney.models.fields import MoneyField
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Service(TimeStampedModel):
    """
    to define a service
    """
    CATEGORY_CHOICES = (
        ('engine', _("Engine System")),
        ('suspension', _("Suspension System")),
        ('transmission', _("Transmission System")),
        ('steering', _("Steering System")),
        ('electric', _("Electric System")),
        ('breaks', _("Brakes system")),
        ('body', _("Car Body")),
    )
    name = models.CharField(
        _('name'),
        max_length=128,
        help_text="Service's name",
    )
    description = models.CharField(
        _('description'),
        default=None,
        max_length=1024,
        help_text="Service description",
    )
    price = MoneyField(
        decimal_places=2,
        default=0,
        default_currency='USD',
        max_digits=8,
    )
    category = models.CharField(
        _('name'),
        default=None,
        max_length=128,
        choices=CATEGORY_CHOICES,
        help_text="Service's category",
    )
