def base_divisor(inputted_value, divisor):
    """Divides the first parameter by the second"""
    quotient = inputted_value / divisor
    return int(quotient)


"""
Return the quotient of the first parameter divided by the second

:param inputted_value: int
:param divisor: int
:precondition: Both parameters must be ints
:postcondition: An integer which is the quotient of the two parameters
:return: The quotient of the first parameter divided by the second 
"""


def base_remainder(divisor_remainder, modulo):
    """Calculates the remainder between the first parameter divided by the second"""
    remainder = divisor_remainder % modulo
    return remainder


"""
Return the remainder of the first parameter divided by the second.

:param divisor_remainder: int
:param modulo: int
:precondition: Both parameters must be int
:postcondition: An integer which is the remainder of the two parameters divided by each other
:return: The remainder of the first parameter divided by the second parameter
"""


def base_conversion():
    """Converts one number in to the base of another number"""
    value = int(input("Destination base (must be from 2 - 9):"))
    destination_value = (value ** 4 - 1)
    new_value = input("The maximum value for this base is " + str(destination_value) +
                      ", enter another value that is equal or lower:")
    digit_1 = base_divisor(int(new_value), value)
    digit_2 = base_divisor(digit_1, value)
    digit_3 = base_divisor(digit_2, value)
# This is where the integers for the base_remainder function are calculated
    converted_number = \
        str(base_remainder(int(new_value), value)) \
        + str(base_remainder(digit_1, value)) \
        + str(base_remainder(digit_2, value)) \
        + str(base_remainder(digit_3, value))
# The number in new_value is converted into the base of the number in value here
    return converted_number


"""
Return the second inputted number in the base of the first inputted number.

:precondition: First inputted value must be an int
:precondition: Second inputted value must be an int
:postcondition: Divide the second inputted value by the first inputted value until four digits are made. 
                Take the remainder of each digit and concatenate them until the base converted number is formed.
:return: The equivalent of the second inputted number (in base 10) to the base determined by the first inputted number    
"""


def main():
    """Executes the program"""
    print(base_conversion())


if __name__ == "__main__":
    main()