
# Assignment 5: Quicksort Algorithm

## Course
MSCS-532: Algorithms and Data Structures

University of the Cumberlands

## Project Overview
This project implements deterministic and randomized Quicksort
algorithms in Python. It analyzes their theoretical time and
space complexity and compares their execution times across
different input sizes and distributions.

## Project Files
- `quicksort.py` - Deterministic Quicksort using an explicit stack.
- `recursive_quicksort.py` - Recursive deterministic Quicksort.
- `randomized_quicksort.py` - Recursive randomized Quicksort.
- `performance_analysis.py` - Benchmarking script.
- `performance_results.csv` - Recorded benchmark results.
- `test_quicksort.py` - Correctness and edge-case tests.
- `MSCS532_Assignment5_Quicksort.pdf` - Academic analysis report.

## Requirements
- Python 3.10 or later
- No third-party packages required

## How to Run

Open a terminal in the project folder.

### Deterministic Quicksort
```bash
python quicksort.py
```

### Recursive Quicksort
```bash
python recursive_quicksort.py
```

### Randomized Quicksort
```bash
python randomized_quicksort.py
```

### Performance Analysis
```bash
python performance_analysis.py
```

This command creates or updates `performance_results.csv`.

### Correctness Tests
```bash
python test_quicksort.py
```

## Experimental Method
The benchmark compares deterministic and randomized Quicksort
on random, sorted, and reverse-sorted arrays containing
100, 500, and 1,000 elements.

Each test is repeated five times, and the median execution
time is recorded in milliseconds.

The benchmark compares `quicksort.py` with
`randomized_quicksort.py`. The separate recursive
deterministic implementation is provided to demonstrate
the recursive algorithm structure.

## Summary of Findings
- Both benchmarked algorithms produced correct sorted results.
- Both implementations passed eight edge-case tests.
- Deterministic last-element pivot selection performed
  poorly on already sorted and reverse-sorted inputs.
- Random pivot selection substantially improved performance
  on these ordered inputs.
- Randomized Quicksort has expected O(n log n) time complexity,
  although its theoretical worst case remains O(n²).
- The results are machine-dependent and may vary between runs.

## Documentation
See `MSCS532_Assignment5_Quicksort.pdf` for the theoretical
analysis, empirical measurements, discussion, and references.
