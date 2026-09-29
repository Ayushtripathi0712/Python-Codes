"""
Filename: pandas_series_random.py
Subject: Python Programming (Introduction to Pandas Series)
Description: Creating a Pandas Series using 10 classroom names with custom roll numbers,
sorting, boolean filtering, and key attributes.
"""

import numpy as np
import pandas as pd


def create_random_series(seed: int = 42) -> pd.Series:
    classroom_names = [
        "Aarav",
        "Ananya",
        "Rohan",
        "Priya",
        "Kabir",
        "Sanya",
        "Vikram",
        "Isha",
        "Aditya",
        "Diya",
    ]
    rng = np.random.default_rng(seed)
    random_indices = rng.integers(low=0, high=len(classroom_names), size=10)
    selected_names = [classroom_names[i] for i in random_indices]
    return pd.Series(selected_names, name="Student_Names")


def create_labeled_series(series: pd.Series) -> pd.Series:
    custom_labels = [f"Roll_{i}" for i in range(101, 111)]
    return pd.Series(data=series.values, index=custom_labels, name="Student_Names")


def describe_series(series: pd.Series) -> None:
    print("Series Output:\n", series, sep="")
    print(f"Data Type (.dtype): {series.dtype}")
    print(f"Shape (.shape):     {series.shape}")
    print(f"Total Size (.size): {series.size}")
    print(f"Index (.index):     {series.index}")
    print("-" * 50)


if __name__ == "__main__":
    random_series = create_random_series(seed=42)
    describe_series(random_series)

    labeled_series = create_labeled_series(random_series)
    describe_series(labeled_series)

    print("Alphabetically First (.min()):", labeled_series.min())
    print("Alphabetically Last (.max()): ", labeled_series.max())
    print("Concatenated Names (.sum()):  ", labeled_series.str.cat(sep=", "))
    print("-" * 50)

    sorted_series = labeled_series.sort_values()
    print("Sorted Series by Name:")
    print(sorted_series)
    print("-" * 50)

    filtered_series = labeled_series[labeled_series > "K"]
    print("Filtered Series (Names > 'K'):")
    print(filtered_series)
    print("-" * 50)

    different_seed_series = create_random_series(seed=100)
    print("Series with Seed = 100:")
    print(different_seed_series)