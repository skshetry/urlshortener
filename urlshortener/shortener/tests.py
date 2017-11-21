"""Tests for `urlshortener`"""
from django.test import TestCase

from .utils import encode_base62, decode_base62


class HelperTest(TestCase):
    def test_encode(self):
        self.assertEqual(encode_base62(76), '1e')

    def test_encode_on_zero(self):
        self.assertEqual(encode_base62(0), '0')

    def test_encode_on_one(self):
        self.assertEqual(encode_base62(1), '1')

    def test_encode_on_negative_numbers_return_none(self):
        self.assertFalse(encode_base62(-10))

    def test_decode(self):
        self.assertEqual(decode_base62('1e'), 76)

    def test_decode_on_zero(self):
        self.assertEqual(decode_base62('0'), 0)

    def test_decode_on_one(self):
        self.assertEqual(decode_base62('1'), 1)

    def test_decode_on_sends_none_on_empty_string(self):
        self.assertFalse(decode_base62(''))
