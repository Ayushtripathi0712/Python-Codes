"""
Techniques:
1. Top-Down Approach (Memoization)
2. Bottom-Up Approach (Tabulation with Item Tracking)
"""

# =====================================================================
# 1. TOP-DOWN APPROACH (MEMOIZATION)
# =====================================================================
def knapsack_memo(weights, values, n, capacity, memo):
    # Base condition: No items left or capacity is 0
    if n == 0 or capacity == 0:
        return 0

    # Check if result is already calculated
    if memo[n][capacity] != -1:
        return memo[n][capacity]

    # If current item is heavier than remaining capacity, exclude it
    if weights[n - 1] > capacity:
        memo[n][capacity] = knapsack_memo(weights, values, n - 1, capacity, memo)
    else:
        # Choice 1: Include the current item
        include = values[n - 1] + knapsack_memo(weights, values, n - 1, capacity - weights[n - 1], memo)
        # Choice 2: Exclude the current item
        exclude = knapsack_memo(weights, values, n - 1, capacity, memo)
        # Store the maximum of both choices
        memo[n][capacity] = max(include, exclude)

    return memo[n][capacity]


# =====================================================================
# 2. BOTTOM-UP APPROACH (TABULATION)
# =====================================================================
def knapsack_tabular(weights, values, capacity):
    n = len(weights)

    # Step 1: Create DP table initialized to 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Step 2: Fill the table iteratively
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                take = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                not_take = dp[i - 1][w]
                dp[i][w] = max(take, not_take)
            else:
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]

    # Step 3: Backtrack to find which items were selected
    selected = []
    curr_w = capacity
    for i in range(n, 0, -1):
        if dp[i][curr_w] != dp[i - 1][curr_w]:
            selected.append(i)  # Item i was included
            curr_w -= weights[i - 1]

    selected.reverse()
    return max_value, selected, dp


# =====================================================================
# MAIN EXECUTION (Matches data in Notes Assignment 6)
# =====================================================================
if __name__ == "__main__":
    # Test Data from Assignment 6 PDF
    weights = [2, 1, 3, 2]
    values = [12, 10, 20, 15]
    capacity = 5
    n = len(weights)

    print("==========================================================")
    print("           ASSIGNMENT 6: 0/1 KNAPSACK PROBLEM             ")
    print("==========================================================")
    print(f"Weights : {weights}")
    print(f"Values  : {values}")
    print(f"Capacity: {capacity}\n")

    # --- Running Top-Down (Memoization) ---
    memo_table = [[-1] * (capacity + 1) for _ in range(n + 1)]
    result_memo = knapsack_memo(weights, values, n, capacity, memo_table)
    print("[1] Top-Down Approach (Memoization):")
    print(f"    Maximum Value = {result_memo}")

    # --- Running Bottom-Up (Tabulation) ---
    result_tab, selected_items, dp_table = knapsack_tabular(weights, values, capacity)
    print("\n[2] Bottom-Up Approach (Tabulation):")
    print(f"    Maximum Value  = {result_tab}")
    print(f"    Selected Items = {['Item ' + str(idx) for idx in selected_items]}")

    # Display the final DP table matching the PDF
    print("\n--- Final DP Table ---")
    header = "Item \\ Cap | " + "  ".join(f"{c:2d}" for c in range(capacity + 1))
    print(header)
    print("-" * len(header))
    for i in range(n + 1):
        row_str = f"Item {i:<5} | " + "  ".join(f"{dp_table[i][c]:2d}" for c in range(capacity + 1))
        print(row_str)
    print("==========================================================")