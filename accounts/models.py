from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from commons.models import TimeStampedModel
import logging


logger = logging.getLogger(__name__)


def get_username(instance):
    return instance.user.get_username()


class User(AbstractUser):
    is_company = models.BooleanField(default=False)


class Account(TimeStampedModel):
    """
    add local account
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_fraud = models.BooleanField(
        _('Is fraud'),
        default=False,
        db_index=True,
        help_text=_('Marks if the user is trying to cheat the system.')
    )
    slug = AutoSlugField(
        unique_with='company__name',
        editable=False,
        populate_from=get_username
    )
    company = models.ForeignKey(
        'companies.Company',
        on_delete=models.CASCADE,
        default=None
    )
    vehicles = models.ForeignKey(
        'vehicles.Vehicle',
        on_delete=models.CASCADE,
        default=None,
    )

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def __str__(self):
        return f"{self.slug}"
