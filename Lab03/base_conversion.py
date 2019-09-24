def base_divisor(inputted_value, divisor):
    quotient = inputted_value / divisor
    return int(quotient)


def base_remainder(divisor_remainder, modulo):
    remainder = divisor_remainder % modulo
    return remainder


def base_conversion():
    value = int(input("Destination base (must be from 2 - 9):"))
    destination_value = (value ** 4 - 1)
    new_value = input("The maximum value for this base is " + str(destination_value) +
                      ", enter another value that is equal or lower:")
    digit_1 = base_divisor(int(new_value), value)
    digit_2 = base_divisor(digit_1, value)
    digit_3 = base_divisor(digit_2, value)
    converted_number = str(base_remainder(int(new_value), value)) \
        + str(base_remainder(digit_1, value)) \
        + str(base_remainder(digit_2, value)) \
        + str(base_remainder(digit_3, value))
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
    print(base_conversion())


"""
Executes the program
"""

if __name__ == "__main__":
    main()