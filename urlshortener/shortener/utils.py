"""Utilities functions for the `shortener` app."""
import string

ALPHABETS: str = string.digits + string.ascii_letters
alphabet_length: int = len(ALPHABETS)

def encode_base62(id_dec: int) ->str:
    result = ''
    while id_dec > 0:
        id_dec, mod = divmod(id_dec, alphabet_length)
        result = ALPHABETS[mod] + result
    return result
