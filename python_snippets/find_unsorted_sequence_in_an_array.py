"""
    Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n,
    the entire array would be sorted. Minimize n - m (that find the smallest sequence)
"""
def find_unsorted_sequence(array):
    # find left subsequence
    end_left = find_end_of_left_subsequence(array)
    if end_left >= len(array) - 1:
        return

    start_right = find_start_of_right_subsequence(array)

    # get min and max
    max_index = end_left
    min_index = start_right
    i = end_left + 1
    while i < start_right:
        if array[i] < array[min_index]:
            min_index = i
        if array[i] > array[max_index]:
            max_index = i
        i += 1

    # Slide left until less than array[min_index]
    left_index = shrink_left(array, min_index, start_right)

    right_index = shrink_right(array, max_index, start_right)

    print(str(left_index) + ' ' + str(right_index))


def find_end_of_left_subsequence(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            return i - 1
    return len(array) - 1


def find_start_of_right_subsequence(array):
    i = len(array) - 2
    # for i in range(len(array)):
    while i >= 0:
        if array[i] > array[i+1]:
            return i + 1
        i -= 1


def shrink_left(array, min_index, start):
    comp = array[min_index]
    i = start - 1
    while i >= 0:
        if array[i] <= comp:
            return i + 1
        i -= 1
    return 0


def shrink_right(array, max_index, start):
    comp = array[max_index]
    i = start
    while i < len(array) - 1:
        if array[i] >= comp:
            return i - 1
        i += 1
    return len(array) - 1


if __name__ == '__main__':
    # find_unsorted_sequence([1, 2 , 4, 7, 10, 11, 8, 12, 5, 6, 16, 18, 19])
    find_unsorted_sequence([1, 2, 3, 5, 4 , 10, 0 ,13 ,14 ,15])