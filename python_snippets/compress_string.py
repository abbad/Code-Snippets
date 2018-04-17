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
