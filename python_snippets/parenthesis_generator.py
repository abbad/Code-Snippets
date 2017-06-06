
def parentheses_generator(open, close, result):
    final_result = []
    if open == 0 and close == 0:
        return [result]

    if close > open:
        final_result += parentheses_generator(open, close - 1, result + ')')
    if open > 0:
        final_result += parentheses_generator(open - 1, close, result + '(')

    return final_result

if __name__ == '__main__':
    res = parentheses_generator(3, 3, '')
    print(res)

    # 1 = ()
    # 2 = ()() (())
    # 3 = ()()() ((())) (())() ()(())
