"""Tests for `urlshortener`."""
from django.test import TestCase

from django.contrib.auth.models import User

from unittest import mock

from .models import Urls
from .utils import encode_base62, decode_base62


class HelperTest(TestCase):
    """Test helper methods for encoding and decoding.

    This class tests encoding/decoding from-to base-62 and base-10 numbers on
    boundary cases.
    """

    def test_encode(self):
        """Test for `encode_base62(id_dec)`."""
        self.assertEqual(encode_base62(76), '1e')

    def test_encode_on_zero(self):
        """Boundary test for zero on `encode_base62`."""
        self.assertEqual(encode_base62(0), '0')

    def test_encode_on_one(self):
        """Boundary Test on one(1). on `encode_base62`."""
        self.assertEqual(encode_base62(1), '1')

    def test_encode_on_negative_numbers_return_none(self):
        """Boundary test on negative numbers on `encode_base62` and ensure it returns `None`."""
        self.assertFalse(encode_base62(-10))

    def test_decode(self):
        """Test for `decode_base62(id_dec)`."""
        self.assertEqual(decode_base62('1e'), 76)

    def test_decode_on_zero(self):
        """Boundary test for zero on `decode_base62`."""
        self.assertEqual(decode_base62('0'), 0)

    def test_decode_on_one(self):
        """Boundary Test on one(1). on `decode_base62`."""
        self.assertEqual(decode_base62('1'), 1)

    def test_decode_on_sends_none_on_empty_string(self):
        """Ensure `decode_base62` sends `None` when empty string is sent.."""
        self.assertFalse(decode_base62(''))


class UrlsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('foo', 'email@example.com', 'bar')
        self.url = Urls.objects.create(
            long_url='https://www.example.com/example1/example2',
            created_by=self.user
            )

    def test_gethash_is_called(self):
        self.assertEqual(self.url.get_hash(), '1')

    def test_str(self):
        self.assertEqual(self.url.__str__(), str(self.url.pk) + ' | ' + self.user.username)

    def test_verbose_name(self):
        self.assertEqual(self.url._meta.verbose_name_plural, 'Urls')