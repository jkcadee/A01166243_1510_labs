import time


def timer(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = function(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        with open('result.txt', 'a+') as file_object:
            file_object.write(f"{run_time:.9f} seconds - {function.__name__!r}\n")
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
    factorial_iterative(500)
    factorial_recursive(995)


if __name__ == '__main__':
    import doctest
    main()
    doctest.testmod()
