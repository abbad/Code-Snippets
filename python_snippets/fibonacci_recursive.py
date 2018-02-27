# TODO: Use dynamic programming.
def fibonacci(number):
    if number == 1:
        return 1
    if number == 0:
        return 0
    return fibonacci(number - 1) + fibonacci(number - 2)

if __name__ == '__main__':
    print(fibonacci(7))
