from django.db import models
from autoslug import AutoSlugField



class Company(TimeStampedModel):
    """
    labeled companies
    """

    name = models.CharField(_('name'), max_length=255)
    slug = AutoSlugField(
        populate_from = 'name',
        unique = True,
        editable = False
    )
    admins = models.ManyToManyField(
        'accounts.Account',
        related_name = 'companies',
        blank = True
    )

    class Meta:
        verbose_name = _('Company'),
        vorbose_name_plural = _('Companies')

    def __str__(self):
        return f"{self.name}"
