def is_balanced(string):
    """
    Check whether a string is made out balanced parenthesis.
    :param string: String made of parentheses, brackets or curly brackets.
    :return: Bool
    """
    if len(string) % 2 != 0 or string == '':
        print(string)
        return False

    stack = []

    right = ['(', '{', '[']
    set = [('(', ')'), ('{', '}'), ('[', ']')]

    for char in string:
        if char in right:
            stack.append(char)
        else:
            if (stack.pop(), char) not in set:
                return False

    return True

if __name__ == '__main__':

    assert is_balanced('') == False
    # Normal case
    assert is_balanced('{{}}[]') == True
    # Odd even balanced
    assert is_balanced('{{}') == False
    # {{(}})
    assert is_balanced('{{(}})') == False

    assert is_balanced('{}}') == False
