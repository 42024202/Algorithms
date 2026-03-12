def countdown(some_int: int) -> None:
    print(some_int)
    if some_int <= 1:
        print("Done")
    else:
        countdown(some_int - 1)


def fact(n: int) -> int:
    """Calculate factorial"""
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)

