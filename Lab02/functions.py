def format_name(first_name, last_name):
    """Execute the program"""
    return first_name.title().lstrip().rstrip() + " " + last_name.title().lstrip().rstrip()


""" 
Return the two parameters with the first character in each word capitalized.

:param first_name: string
:param last_name: string
:precondition: first_name must be a string
:precondition: last_name must be a string
:postcondition: capitalize the first character in first_name and last_name
:return: string with first character in each word capitalized
"""


def tripler(any_parameter):
    """Execute the program"""
    return str(any_parameter * 3)


"""
Return the parameter multiplied by three as a string.

:param any_parameter: any data type
:postcondition: multiply the parameter by three
:return: a data type multiplied by three
"""


def this_year(m, c, d, y):
    """Execute the program"""
    return int((m * c + d) / y)


"""
Return the parameters as a sum of their operators.

:param m: int 
:param c: int
:param d: int
:param y: int
:precondition: m must be int 4
:precondition: c must be int 1000
:precondition: d must be int 38
:precondition: y must be int 2
:postcondition: multiply m and c plus d then divided by y
:return: the sum of m, c, d, and y as produced by their operators
"""


def base_conversion():
    """Execute the program"""
    value = int(input("Destination base (must be from 2 - 9):"))
    destination_value = (value ** 4 - 1)
    new_value = input("The maximum value for this base is " + str(destination_value) +
                      ", enter another value that is equal or lower:")
    digit_1 = int(new_value) / value
    digit_2 = digit_1 / value
    digit_3 = digit_2 / value
    digit_4 = digit_3 / value
    converted_number = int(str(int(digit_3 % value))
                           + str(int(digit_2 % value))
                           + str(int(digit_1 % value))
                           + str(int(int(new_value) % value)))
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
    """Execute the program"""
    print(format_name("   scott   ", "   lang   "))
    print(tripler("python"))
    print(this_year(4, 1000, 38, 2))
    print(base_conversion())


if __name__ == "__main__":
    main()
