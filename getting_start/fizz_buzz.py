numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def solve():
    """Get numbers and print fizz buzz

    Args:
        None

    Returns:
        Void
    """
    for i in numbers:
        if i % 15 == 0:
            print("fizz buzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

        print("\n")


solve()
