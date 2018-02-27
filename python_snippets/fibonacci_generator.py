# python 3.x
def fibonacci():
    """ returns Fibonacci sequence. """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fibonacci_recursive_generator(a=0, b=1):
    """
        returns Fibonacci sequence recursively.
    """
    yield a
    yield from fibonacci_recursive_generator(b, a + b)


if __name__ == '__main__':

    gen = fibonacci_recursive_generator()
    counter = 10
    for v in gen:
        print(v)

        if counter == 0:
            break
        counter -= 1
