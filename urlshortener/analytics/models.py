"""Models for `analytics`."""
from django.db import models


class Analytics(models.Model):
    """Model to track no. of views for a given link and other metadata."""

    views_num = models.IntegerField(default=0)

    def add_one_view(self):
        """Add one to the `views_num`."""
        self.views_num += 1

    def __str__(self):
        """Return string representation. Mostly for Django Admin and Python Shell."""
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Analytics'
