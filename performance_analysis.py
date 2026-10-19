
import csv
import random
import statistics
import time

from quicksort import quicksort
from randomized_quicksort import randomized_quicksort


def measure_time(algorithm, data, repetitions=5):
    """Return median execution time in milliseconds."""
    timings = []

    for _ in range(repetitions):
        test_data = data.copy()

        start = time.perf_counter()
        result = algorithm(test_data)
        elapsed = time.perf_counter() - start

        assert result == sorted(data), "Sorting failed!"
        timings.append(elapsed * 1000)

    return statistics.median(timings)


def run_experiments():
    sizes = [100, 500, 1000]
    distributions = ["Random", "Sorted", "Reverse Sorted"]
    results = []

    for size in sizes:
        for distribution in distributions:
            if distribution == "Random":
                data = random.sample(range(size * 10), size)
            elif distribution == "Sorted":
                data = list(range(size))
            else:
                data = list(range(size, 0, -1))

            deterministic_time = measure_time(quicksort, data)
            randomized_time = measure_time(
                randomized_quicksort, data
            )

            results.append([
                size,
                distribution,
                round(deterministic_time, 4),
                round(randomized_time, 4),
            ])

            print(
                f"Size: {size}, "
                f"Distribution: {distribution}, "
                f"Deterministic: {deterministic_time:.4f} ms, "
                f"Randomized: {randomized_time:.4f} ms"
            )

    with open(
        "performance_results.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow([
            "Input Size",
            "Distribution",
            "Deterministic Time (ms)",
            "Randomized Time (ms)",
        ])
        writer.writerows(results)

    print("\nResults saved to performance_results.csv")


if __name__ == "__main__":
    run_experiments()
