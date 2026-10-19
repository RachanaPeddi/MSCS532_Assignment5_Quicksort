
def recursive_quicksort(arr):
    """Sort a list recursively using the last element as pivot."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = arr[-1]
    smaller = []
    equal = []
    larger = []

    for value in arr:
        if value < pivot:
            smaller.append(value)
        elif value > pivot:
            larger.append(value)
        else:
            equal.append(value)

    return (
        recursive_quicksort(smaller)
        + equal
        + recursive_quicksort(larger)
    )


if __name__ == "__main__":
    numbers = [10, 7, 8, 9, 1, 5]
    print("Original array:", numbers)
    print("Sorted array:", recursive_quicksort(numbers))
