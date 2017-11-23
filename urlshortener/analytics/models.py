"""Models for `analytics`."""
from django.db import models


class Analytics(models.Model):
    views_num = models.IntegerField(default=0)

    def add_one_view(self):
        self.views_num += 1

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name_plural = 'Analytics'
