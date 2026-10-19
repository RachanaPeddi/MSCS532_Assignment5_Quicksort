
def quicksort(arr):
    """Sort a list using deterministic Quicksort."""
    if len(arr) <= 1:
        return arr.copy()

    result = []
    pending = [("sort", arr)]

    while pending:
        operation, values = pending.pop()

        if operation == "emit":
            result.extend(values)
            continue

        if len(values) <= 1:
            result.extend(values)
            continue

        pivot = values[-1]

        smaller = []
        equal = []
        larger = []

        for value in values:
            if value < pivot:
                smaller.append(value)
            elif value > pivot:
                larger.append(value)
            else:
                equal.append(value)

        pending.append(("sort", larger))
        pending.append(("emit", equal))
        pending.append(("sort", smaller))

    return result


if __name__ == "__main__":
    numbers = [10, 7, 8, 9, 1, 5]

    print("Original array:", numbers)
    print("Sorted array:", quicksort(numbers))
