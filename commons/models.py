from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    Abstract base classs,  for common self-update fields,
    created_at ,
    updated_at,
    """

    created_at = models.DateTimeField(
        _('Created At'),
        auto_now_add=True
    )
    last_modified_at = models.DateTimeField(
        _('Last modified at'),
        auto_now=True
    )

    class Meta:
        abstract = True
