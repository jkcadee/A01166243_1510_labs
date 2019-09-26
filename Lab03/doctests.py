import doctest


def base_divisor(inputted_value, divisor):
    """Divides the first parameter by the second.

    >>> base_divisor(4, 2)
    2
    >>> base_divisor(2, 1)
    2
    """
    quotient = inputted_value / divisor
    return int(quotient)


def base_remainder(divisor_remainder, modulo):
    """Calculates the remainder between the first parameter divided by the second
    >>> base_remainder(3, 5)
    3
    >>> base_remainder(5, 6)
    5
    """
    remainder = divisor_remainder % modulo
    return remainder


if __name__ == "__main__":

    doctest.testmod()
