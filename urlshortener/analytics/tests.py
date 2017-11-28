"""Tests for `analytics` package."""
from django.test import TestCase

from analytics.models import Analytics


class AnalyticsTestCase(TestCase):
    """Tests for `Analytics` :model:."""

    def setUp(self):
        """Create a instance of `Analytics` before testing."""
        self.analytics = Analytics.objects.create()

    def test_add_one(self):
        """Test `add_one_view()` :method:."""
        self.analytics.add_one_view()
        self.assertEqual(self.analytics.views_num, 1)

    def test_has_verbose_name_plural(self):
        """Test if `Analytics` :model: contains `verbose_name_plural` on `Meta` :subclass:."""
        self.assertEqual(self.analytics._meta.verbose_name_plural, 'Analytics')
