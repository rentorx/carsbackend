from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from commons.models import TimeStampedModel
import logging


logger = logging.getLogger(__name__)


def get_username(instance):
    return instance.user.get_username()


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
    is_company = models.BooleanField(
        _('Is company'),
        default=False,
        db_index=True,
        help_text=_('Marks if the user is owner is a service provider.')
    )
    slug = AutoSlugField(
        unique_with='company__name',
        editable=False,
        populate_from=get_username
    )
    company = models.ManyToManyField(
        'companies.Company',
        help_text=_('Companies related to this account'),
        related_name='accounts',
        default=None,
        blank=True,
    )


    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')
        #unique_together = (("user"), ("vehicles"))

    def __str__(self):
        return f"{self.slug}"
