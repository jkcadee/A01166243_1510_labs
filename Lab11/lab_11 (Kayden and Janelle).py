import time


def timer(function):
    """Write the runtime of the decorated function in results.txt.

    :param function: Function.
    :precondition: Must be a function.
    :postcondition: Writes the runtime of the decorated function.
    :return: The wrapper function.
    """
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = function(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        with open('result.txt', 'a+') as file_object:
            file_object.write(f"{run_time:.9f} seconds - {function.__name__!r} calculated that "
                              f"{str(args).replace(',', '')[1:-1]}! = {value}\n")
        return value
    return wrapper


@timer
def factorial_iterative(upper):
    """Calculate the factorial of the upper number using iteration.

    :param upper: Integer.
    :precondition: Upper must be positive.
    :return: The factorial of upper.
    """
    result = 1
    i = 2
    while i <= upper:
        result *= i
        i += 1
    return result


def factorial_recursive_helper(num):
    """Calculate the factorial of the upper number using recursion.

    :param num: Integer.
    :precondition: Num must be positive.
    :return: The factorial of num.

    >>> factorial_recursive_helper(5)
    120
    >>> factorial_recursive_helper(10)
    3628800
    """
    return num * factorial_recursive_helper(num - 1) if num > 1 else num


@timer
def factorial_recursive(upper):
    """Calculate the factorial of the upper number using recursion.

    :param upper: Integer.
    :precondition: Upper must be positive.
    :return: The factorial of upper.
    """
    return factorial_recursive_helper(upper)


def main():
    """Runs the functions in the program."""
    for number in range(1, 101):
        factorial_iterative(number)
        factorial_recursive(number)


if __name__ == '__main__':
    import doctest
    main()
    doctest.testmod()
