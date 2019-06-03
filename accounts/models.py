from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
import logging


# Create your models here.

logger = logging.getLogger(__name__)


def get_username(instance):
    return instance.user.get_username()


class Account(models.Model):
    """
    add local account
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_fraud = models.BooleanField(
        _('Is fraud'),
        default = False,
        db_index = True,
        populate_from = get_username
    )

    slug = AutoSlugField(
        unique_with = 'company__name',
        editable = False,
        populate_from = get_username
    )

    company = models.ForeignKey('companies.Company',
        on_delete = models.CASCADE
    )

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def __str__(self):
        return f'{self.slug}'

