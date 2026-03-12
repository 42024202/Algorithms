array = [1,4,6,8,2,3]


def find_min(array: list) -> int:
    """find min int in array and return his index"""    
    smallest = array[0]
    smallest_index = 0
    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def select_sort(array: list) -> list:
    """retrun list after select sort"""
    new_array = []
    copied_array = list(array) 
    for i in range(len(copied_array)):
        smallest = find_min(copied_array)
        new_array.append(copied_array.pop(smallest))
    print(new_array)
    return new_array

select_sort(array)

