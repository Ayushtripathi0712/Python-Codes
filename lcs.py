"""
CALCULATING THE LONGEST COMMON SUBSEQUENCE (LCS) EFFICIENTLY
Approaches: Naive Recursion, Memoized DP (Top-Down), Iterative DP (Bottom-Up with Backtracking)
Tested on: Short sequence (PDF example), Medium DNA sequences
"""

import sys
import timeit

# 1. Increase recursion limit for deep top-down recursion
sys.setrecursionlimit(200000)


# APPROACH 1: NAIVE RECURSION - O(2^(m+n)) Exponential (Safe only for small strings)
def lcs_recursive(X, Y, i=None, j=None):
    if i is None:
        i = len(X)
    if j is None:
        j = len(Y)

    # Base Case: Either string is exhausted
    if i == 0 or j == 0:
        return 0

    # If characters match, move diagonally
    if X[i - 1] == Y[j - 1]:
        return 1 + lcs_recursive(X, Y, i - 1, j - 1)

    # If characters differ, take the maximum of top and left choices
    return max(lcs_recursive(X, Y, i - 1, j), lcs_recursive(X, Y, i, j - 1))


# APPROACH 2: MEMOIZED RECURSION (Top-Down DP) - O(m * n) Time, O(m * n) Space
def lcs_memo(X, Y, i=None, j=None, memo=None):
    if i is None:
        i = len(X)
    if j is None:
        j = len(Y)
    if memo is None:
        memo = {}

    # Base Case
    if i == 0 or j == 0:
        return 0

    state = (i, j)
    if state in memo:
        return memo[state]

    # Recurrence relation
    if X[i - 1] == Y[j - 1]:
        memo[state] = 1 + lcs_memo(X, Y, i - 1, j - 1, memo)
    else:
        memo[state] = max(
            lcs_memo(X, Y, i - 1, j, memo),
            lcs_memo(X, Y, i, j - 1, memo)
        )

    return memo[state]


# APPROACH 3: ITERATIVE TABULATION (Bottom-Up DP) - O(m * n) Time & Space (Recommended)
# Returns both the length and the reconstructed subsequence string
def lcs_dp(X, Y):
    m = len(X)
    n = len(Y)

    # Step 1: Create DP table with (m+1) x (n+1) initialized to 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill table using the standard rules
    # SAME     -> DIAGONAL + 1
    # DIFFERENT-> MAX(TOP, LEFT)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: Backtrack from dp[m][n] to reconstruct the actual LCS string
    lcs_chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_chars.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs_sequence = "".join(reversed(lcs_chars))
    return dp[m][n], lcs_sequence


if __name__ == "__main__":
    # Test cases including the examples from the PDF notes
    test_cases = [
        ("PDF Example 1", "ABC", "AC"),
        ("PDF Example 2", "ABCDGH", "AEDFHR"),
        ("Medium Benchmark", "ACCGTTAGGCT", "AGCTAGGCTAC"),
    ]

    print("==========================================================")
    print("        BENCHMARKING EFFICIENT LCS ALGORITHMS             ")
    print("==========================================================")

    for label, s1, s2 in test_cases:
        m, n = len(s1), len(s2)
        print(f"\n---> Testing Case: {label} (X='{s1}', Y='{s2}')")

        # 1. Naive Recursive (Only for short lengths <= 15)
        if m <= 15 and n <= 15:
            t_rec = timeit.timeit(lambda: lcs_recursive(s1, s2), number=1)
            print(f" [1] Naive Recursion    : Time = {t_rec:.6f} sec")
        else:
            print(f" [1] Naive Recursion    : Skipped (Exponential O(2^(m+n)))")

        # 2. Top-Down Memoized DP
        t_memo = timeit.timeit(lambda: lcs_memo(s1, s2), number=1)
        print(f" [2] Memoized DP        : Time = {t_memo:.6f} sec")

        # 3. Bottom-Up Iterative DP
        t_dp = timeit.timeit(lambda: lcs_dp(s1, s2), number=1)
        length, sequence = lcs_dp(s1, s2)
        print(f" [3] Iterative DP       : Time = {t_dp:.6f} sec")

        print(f" Result: LCS Length = {length} | Subsequence = '{sequence}'")

    print("\n==========================================================")
    # Interactive verification matching the user input in the PDF
    print("Interactive Test (Press Enter to test with custom input):")
    user_x = input("Enter first sequence (or press Enter for 'ABC'): ") or "ABC"
    user_y = input("Enter second sequence (or press Enter for 'AC'): ") or "AC"
    res_len, res_seq = lcs_dp(user_x, user_y)
    print(f"Length of LCS: {res_len}")
    print(f"LCS Sequence : {res_seq}")
    print("==========================================================")