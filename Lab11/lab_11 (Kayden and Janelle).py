import time


def timer(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        value = function(*args, **kwargs)
        end = time.perf_counter()
        run_time = end - start
        with open('result.txt', 'a+') as file_object:
            file_object.write(f"{function.__name__!r}: {run_time:.4f} seconds")
        return value
    return wrapper

