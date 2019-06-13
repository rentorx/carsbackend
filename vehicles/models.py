from django.db import models
from commons.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
import logging

logger = logging.getLogger(__name__)


# Create your models here.


class Vehicle(TimeStampedModel):
    """
    labeled Vehicles
    """

    plates = models.CharField(_('plates'), max_length=32)
    brand = models.CharField(_('brand'), max_length=32)
    type = models.CharField(_('type'), max_length=32)
    model = models.CharField(_('model'), max_length=32)

    class Meta:
        verbose_name = _('vehicle'),
        verbose_name_plural = _('vehicles')

    def __str__(self):
        return f"{self.plates}"
