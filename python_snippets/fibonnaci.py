# TODO: Use dynamic programming.
def fibonnaci(number):
    if number == 1:
        return 1
    if number == 0:
        return 0
    return fibonnaci(number - 1) + fibonnaci(number - 2)

if __name__ == '__main__':
    print(fibonnaci(7))
