"""Utilities functions for the `shortener` app."""
import string

ALPHABETS: str = string.digits + string.ascii_letters
alphabet_length: int = len(ALPHABETS)


def encode_base62(id_dec: int) ->str:
    """Convert base-10 numerals to base-62 numerals.

    This uses the same algorithm we use on conversion
    of decimal to binary numbers, i.e. divide by the to-be converted radix.
    """
    if id_dec == 0:
        # Return first char, no need to compute for this.
        return ALPHABETS[0]

    result = ''
    while id_dec > 0:
        id_dec, mod = divmod(id_dec, alphabet_length)
        result = ALPHABETS[mod] + result
    return result

def decode_base62(id_str: str) -> int:
    """Convert base-62 numerals to base-10 numerals."""
    if id_str:
        sum_total = 0
        for power, char in enumerate(reversed(id_str)):
            sum_total += ALPHABETS.index(char) * pow(alphabet_length, power)
        return sum_total
