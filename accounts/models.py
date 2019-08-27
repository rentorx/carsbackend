import logging
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from autoslug import AutoSlugField
from commons.models import TimeStampedModel


logger = logging.getLogger(__name__)


def get_username(instance):
    return instance.user.get_username()


class Account(TimeStampedModel):
    """
    add local account
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), unique=True, blank=False)

    is_fraud = models.BooleanField(
        _('Is fraud'),
        default=False,
        db_index=True,
        help_text=_('Marks if the user is trying to cheat the system.')
    )
    is_owner = models.BooleanField(
        _('Is owner'),
        default=False,
        db_index=True,
        help_text=_('Marks if the user is owner is a service provider.')
    )
    company = models.ForeignKey(
        'companies.Company',
        help_text=_('Companies related to this account'),
        default=None,
        related_name='accounts',
        on_delete=models.CASCADE
    )
    slug = AutoSlugField(
         unique_with='company__name',
         editable=False,
        populate_from=get_username
    )

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

        #unique_together = (("user"), ("vehicles"))

    def __str__(self):
        return f"{self.user.username}"

    @property
    def full_name(self):
        return f'{self.user.last_name} {self.user.first_name}'

    @property
    def email(self):
        return f'{self.user.email}'

    def save(self, *args, commit=True, **kwargs):
        logger.info('saving user')
        #if self.id:
        return super().save(*args, **kwargs)
