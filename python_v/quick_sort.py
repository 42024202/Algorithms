list1 = [1,2,7,4,5,6,2]

def sum_list(array: list) -> int:
    """Requrse function to sum list"""
    if len(array) == 1:
        return array[0]
    else:
        return array[0] + sum_list(array[1:])


def count_list(array: list) -> int:
    """Requrse function to count elements in list"""
    if len(array) == 1:
        return 1
    else:
        return 1 + count_list(array[1:])


def find_max_int(array: list) -> int:
    """Requrse function to find max int in list"""
    if len(array) == 2:
        return (array[0] if array[0] > array[1] else array[1])
    else:
        return (array[0] if array[0] > find_max_int(array[1:]) else find_max_int(array[1:]))

