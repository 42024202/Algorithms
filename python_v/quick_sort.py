
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
    if len(array) == 1:
        return array[0]
    max_int = find_max_int(array[1:])
    return (max_int if max_int > array[0] else array[0])
    
    #First verions:
    if len(array) == 2:
        return (array[0] if array[0] > array[1] else array[1])
    else:
        return (array[0] if array[0] > find_max_int(array[1:]) else find_max_int(array[1:]))


def quick_sort(array: list) -> list:
    """Quick sort algorithm"""
    if len(array) < 2:
        return array
    else:
        support_element = array[0]
        bigger = [i for i in array[1:] if i > support_element]
        smaller = [i for i in array[1:] if i < support_element]
        
        return quick_sort(smaller) + [support_element] + quick_sort(bigger)

print(quick_sort([1,4,6,8,2,3]))

