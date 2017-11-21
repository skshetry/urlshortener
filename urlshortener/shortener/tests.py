"""Tests for `urlshortener`"""
from django.test import TestCase

from .utils import encode_base62, decode_base62


class HelperTest(TestCase):
    def test_encode(self):
        self.assertEqual(encode_base62(76), '1e')

    def test_decode(self):
        self.assertEqual(decode_base62('1e'), 76)
