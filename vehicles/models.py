from django.db import models
from commons.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator
import logging
import datetime

logger = logging.getLogger(__name__)


class Vehicle(TimeStampedModel):
    """
    labeled Vehicles
    """
    BRAND_CHOICES = (
        ('honda', _("Honda")),
        ('bmw', _("BMW")),
        ('kia', _("kia")),
        ('mazda', _("Mazda")),
        ('vw', _("Volkswagen")),
        ('tesla', _("Tesla")),
        ('nissan', _("Nissan")),
    )
    plates = models.CharField(
        _('plates'),
        max_length=32
    )
    brand = models.CharField(
        _('brand'),
        default="vw",
        choices=BRAND_CHOICES,
        max_length=12,
    )
    type = models.CharField(_('type'), max_length=32)
    model = models.PositiveIntegerField(
        _('model'),
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(datetime.datetime.now().year + 1)
        ],
        default=datetime.datetime.now().year,
        help_text="Model year format: <YYYY>"
    )
    account = models.ForeignKey(
        'accounts.Account',
        on_delete=models.CASCADE,
        help_text=_('Account owner for this vehicle'),
        default=None,
    )

    class Meta:
        verbose_name = _('vehicle'),
        verbose_name_plural = _('vehicles')
        unique_together = (("plates", "account"),)

    def __str__(self):
        return f"{self.plates}"
