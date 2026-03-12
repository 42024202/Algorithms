def binary_search_func(array: list, target: int) -> int:
    low: int = 0
    high: int = len(array) - 1
    tryes: int = 0
    
    while low <= high:
        mid: int = (low + high) // 2
        guess = array[mid]
        if guess < target:
            low = mid + 1
        elif guess > target:
            high = mid -1
        elif guess == target:
            print(f"Your number is at index {mid}")
            break
        print(f"Tryes: {tryes}")
        tryes += 1
    return 0

list1 = [1,2,3,4,5,6,7,8,9,10]
binary_search_func(list1, 7)

