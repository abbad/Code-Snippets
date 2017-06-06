
def generate(string, start, end):
    result = []
    if start == end - 1:
        if string not in result:
            return [string]
    else:
        for current in range(start, end):
            x = list(string)
            # Swap values.
            temp = x[start]
            x[start] = x[current]
            x[current] = temp
            # Call generate function again.
            result += generate(''.join(x), start + 1, end)
            # Swap values again.
            temp = x[start]
            x[start] = x[current]
            x[current] = temp
    return result

# ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
# ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']

if __name__ == '__main__':
    result = generate('aac', 0, 3)
    print(result)
