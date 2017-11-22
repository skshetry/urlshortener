from django.test import TestCase

from .models import Analytics


class AnalyticsTestCase(TestCase):
    def setUp(self):
        self.analytics = Analytics.objects.create()

    def test_str(self):
        self.assertEqual(self.analytics.__str__(), '1')

    def test_add_one(self):
        self.analytics.add_one_view()
        self.assertEqual(self.analytics.views_num, 1)

    def test_has_verbose_name_plural(self):
        self.assertEqual(self.analytics._meta.verbose_name_plural, 'Analytics')
