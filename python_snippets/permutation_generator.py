

def generate_perm(string, step, result):

    if step == len(string):
        print(string)
        result.append(string)
        return
    for index in range(step, len(string)):

        # swap parts item at index with item at step
        string = list(string)
        string[step], string[index] = string[index], string[step]

        string = "".join(string)

        generate_perm(string, step + 1, result)


# ['abc', 'acb', 'bac', 'bca', 'cba', 'cab']
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

if __name__ == '__main__':
    perms = []
    generate_perm('abcd', 0, perms)
    print(perms)
