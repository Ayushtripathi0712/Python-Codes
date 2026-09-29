import numpy as np


# Step 3: Create array using np.array() from a Python list
def create_array_from_list():
    return np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Step 4: Create array using np.arange()
def create_array_with_arange():
    return np.arange(1, 11)  # stop value 11 is excluded


# Step 5: Function to print array details and key attributes
def describe_array(arr):
    print("Array:", arr)
    print("Data Type (.dtype):", arr.dtype)
    print("Shape (.shape):", arr.shape)
    print("Dimensions (.ndim):", arr.ndim)
    print("Size (.size):", arr.size)
    print("-" * 40)


# Step 6: Main execution block
if __name__ == "__main__":
    print("=== Step 6: Creating and Describing Arrays ===")
    arr_list = create_array_from_list()
    arr_range = create_array_with_arange()

    print("--- Array from List ---")
    describe_array(arr_list)

    print("--- Array from arange ---")
    describe_array(arr_range)

    # Step 7: Confirm both methods produce equal arrays
    are_equal = np.array_equal(arr_list, arr_range)
    print("=== Step 7: Array Equality Check ===")
    print(f"Are both arrays equal? {are_equal}\n")

    # Step 8: Vectorized operations
    print("=== Step 8: Vectorized Operations ===")
    print("arr * 2:    ", arr_range * 2)
    print("arr + 100:  ", arr_range + 100)
    print("arr.sum():  ", arr_range.sum())
    print("arr.mean(): ", arr_range.mean())
    print()

    # Step 9: Indexing and Slicing
    print("=== Step 9: Indexing and Slicing ===")
    print("First element (arr[0]):    ", arr_range[0])
    print("Last element (arr[-1]):    ", arr_range[-1])
    print("First 5 elements (arr[:5]):", arr_range[:5])
    print("Every second element (arr[::2]):", arr_range[::2])
    print()

    # Step 11: Array from 1 to 20
    print("=== Step 11: Modified Array (1 to 20) ===")
    arr_20 = np.arange(1, 21)
    describe_array(arr_20)