"""
Write a function that accepts a string with some number of consecutive repeating 
characters and returns a copy of the string with consecutive repeating characters 
replaced by a count of the repetitions. 
 
 "sssssTTTTTTops" ? "s5T6ops" 
"""
 

def compress_string(string):
    """
    :param string:
    :return:
    """
    result = string[:1]
    count = 1

    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            count += 1
        else:
            if count > 1:
                result += str(count)
            result += string[index + 1]
            count = 1

    if count > 1:
        result += str(count)

    return result


def compress_string_with_dict(str):
    """
    different solution.
    """
    count_keeper = {}

    for char in str:
        if char in count_keeper:
            count_keeper[char] += 1
        else:
            count_keeper[char] = 1

    result = ''

    for key in count_keeper:
        if count_keeper[key] == 1:
            result = f"{result}{key}"  
        else:
            result = f"{result}{key}{count_keeper[key]}"

    if len(result) > len(str):
        return str
    return result


assert compress_string('aaa') == 'a3'
assert compress_string('aaaabc') == 'a4b1c1'

assert compress_string('abc') == 'abc'

