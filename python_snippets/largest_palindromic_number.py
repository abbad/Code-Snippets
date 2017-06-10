"""
    This is a random question from project euler.
    1. A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

"""
def find_largest_palindrome():
    array_list = list()
    for x in range(1,999):
        for y in range(1, 999):
            array_list.append(x * y)

    largest_palindrome = None
    for x in array_list:
        if x == array_list[0]:
            largest_palindrome = array_list[0]

        if is_palindrome(x) and x > largest_palindrome:
            largest_palindrome = x

    return largest_palindrome


def is_palindrome(number):
    str_number = str(number)
    length = len(str_number) - 1
    for char in str_number[:len(str_number)//2]:
        if char == str_number[length]:
            length -= 1
        else:
            return False

    return True

if __name__ == "__main__":
    print(find_largest_palindrome())
