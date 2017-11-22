"""Models for urlshortener."""
from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self) -> str:
        """Return string representation. Mostly for Django Admin and Python Shell."""
        return str(self.pk) + ' | ' + self.created_by.get_username()
