__author__ = 'Abbad'


def bubble_sort(array):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for index in range(1, len(array)):
            if array[index - 1] > array[index]:
                # swap
                is_sorted = False
                temp = array[index - 1]
                array[index - 1] = array[index]
                array[index] = temp

    return array


if __name__ == '__main__':

    print(bubble_sort([3,2,1]))