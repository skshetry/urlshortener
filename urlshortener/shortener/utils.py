"""Utilities functions for the `shortener` app."""
import string

ALPHABETS: str = string.digits + string.ascii_letters
alphabet_length: int = len(ALPHABETS)

def encode_base62(id_dec: int) ->str:
    if id_dec==0:
        return ALPHABETS[0]

    result = ''
    while id_dec > 0:
        id_dec, mod = divmod(id_dec, alphabet_length)
        result = ALPHABETS[mod] + result
    return result

def decode_base62(id_str: str) -> int:
    if id_str:
        sum_total = 0
        for power, char in enumerate(reversed(id_str)):
            sum_total += ALPHABETS.index(char) * pow(alphabet_length, power)
        return sum_total
