"""Utilities."""

from fractions import Fraction


def format_fraction(
    fraction: Fraction,
    vinculum: str = ":",
    exponential: bool = False,
    decimal_seperator: str = ",",
) -> str:
    """Format fraction.

    Format a fraction for presentation. Default values are suitable for a scale ratio.

    :param fraction: The Fraction to be formated
    :param vinculum: The Fraction seperator
    :param exponential: Abbreviate denominator by using exponent notation
    :param decimal_seperator: Decimal seperator to use for the denominator

    :return: Fraction formatted as a string
    """
    if exponential:
        return f"{fraction.numerator:}{vinculum}{fraction.denominator:.0e}"

    return f"{fraction.numerator}{vinculum}{fraction.denominator:{decimal_seperator}}"
