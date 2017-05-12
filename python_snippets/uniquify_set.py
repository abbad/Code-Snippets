'''

Transform the following list of items into the one below.
Input: ['nutella', 'cake', 'chocolate', 'chips']
Output: ['n', 'ca', 'cho', 'chi']
'''


def uniquify(org_list, item):
    string_range = 1
    result_string = item[0]

    for val in org_list:
        flag = True
        if val != item:
            while flag:
                target_string = val[:string_range]
                if result_string == target_string:
                    string_range += 1
                    result_string = item[:string_range]
                else:
                    flag = False
                    continue

    return result_string


def get_shopping_list(org_list):
    """
        A function that takes a list and returns
        a shorter list.
    """
    # Iterate over the items.
    result = []
    for item in org_list:
        # Check if character is unique within the list.
        result.append(uniquify(org_list, item))

    return result

if __name__ == '__main__':
    org_list = ['nutella', 'cake', 'chocolate', 'chips']
    shortened_list = get_shopping_list(org_list)
    print(shortened_list)