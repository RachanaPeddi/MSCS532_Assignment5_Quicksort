
from quicksort import quicksort
from randomized_quicksort import randomized_quicksort


def test_algorithms():
    test_cases = [
        [],
        [5],
        [3, 1, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [4, 4, 2, 2, 1],
        [-5, 3, 0, -1, 8],
        [7, 7, 7, 7],
    ]

    for algorithm in [quicksort, randomized_quicksort]:
        for case in test_cases:
            original = case.copy()
            result = algorithm(case)

            assert result == sorted(original), (
                f"{algorithm.__name__} failed: {case}"
            )
            assert case == original, (
                f"{algorithm.__name__} modified the input"
            )

        print(
            f"PASS: {algorithm.__name__} "
            f"passed all {len(test_cases)} tests."
        )


if __name__ == "__main__":
    test_algorithms()
