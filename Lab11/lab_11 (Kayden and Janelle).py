import time
import doctest


def timer(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = function(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        with open('result.txt', 'a+') as file_object:
            file_object.write(f"{function.__name__!r}: {run_time:.12f} seconds\n")
        return value
    return wrapper


def factorial_iterative(upper):
    """
    Return the factorial of between 1 and the upperbound number.

    :param upper: Integer.
    :precondition: Upper must be positive.
    :return: The factorial between 1 and upperbound.
    """
    result = 1
    i = 2
    while i <= upper:
        result *= i
        i += 1
    return result


# def factorial_recursive():
