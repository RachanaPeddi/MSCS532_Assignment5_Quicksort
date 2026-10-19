
import random


def randomized_quicksort(arr):
    """Sort a list using a randomly selected pivot."""
    if len(arr) <= 1:
        return arr.copy()

    pivot = random.choice(arr)

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
        randomized_quicksort(smaller)
        + equal
        + randomized_quicksort(larger)
    )


if __name__ == "__main__":
    numbers = [10, 7, 8, 9, 1, 5]

    print("Original array:", numbers)
    print("Randomized sorted array:", randomized_quicksort(numbers))
