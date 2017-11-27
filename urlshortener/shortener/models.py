"""Models for urlshortener."""
from django.db import models

from django.contrib.auth.models import User

from analytics.models import Analytics

from shortener.utils import encode_base62


class Urls(models.Model):
    """Models for urls."""

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    url_title = models.TextField(default='')
    long_url = models.URLField()
    created_by = models.ForeignKey(
        to=User,
        related_name='user_links',
        null=True, blank=True
        )
    analytics = models.OneToOneField(
        to=Analytics, on_delete=models.CASCADE,
        primary_key=True,
        )

    def save(self, *args, **kwargs):
        """Create analytics beforehand saving. """
        self.analytics = Analytics.objects.create()
        super(Urls, self).save(*args, **kwargs)

    def get_hash(self) -> int:
        """Get hash from the `self.pk`."""
        return encode_base62(id_dec=self.pk)

    def __str__(self) -> str:
        """Return string representation. Mostly for Django Admin and Python Shell."""
        return str(self.pk) + ' | ' + self.created_by.get_username()

    class Meta:
        verbose_name_plural = 'Urls'