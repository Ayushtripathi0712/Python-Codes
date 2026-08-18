"""
 CALCULATING THE NTH FIBONACCI NUMBER EFFICIENTLY
 Approaches: Naive Recursion, Memoized DP, Iterative DP, Fast Doubling
 Tested on: n = 100, n = 1000, n = 100000

"""
import sys
import timeit

# 1. Increase recursion limit for memoization
sys.setrecursionlimit(200000)

# 2. Increase integer-to-string conversion limit (Fixes ValueError for n = 100000)
if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(300000)


# NAIVE RECURSION - O(2^n) Exponential (Only safe for small n <= 30)
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# MEMOIZED RECURSION (Top-Down DP) - O(n) time
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ITERATIVE TABULATION (Bottom-Up DP) - O(n) time, O(1) space (Recommended)
def fib_dp(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# FAST DOUBLING - O(log n) time (Fastest for massive n)
def fib_fast_doubling(n):
    def _fib_pair(k):
        if k == 0:
            return (0, 1)
        a, b = _fib_pair(k // 2)
        c = a * (2 * b - a)
        d = a * a + b * b
        if k % 2 == 0:
            return (c, d)
        else:
            return (d, c + d)

    return _fib_pair(n)[0]


if __name__ == "__main__":
    target_values = [100, 1000, 100000]

    print("==========================================================")
    print("      BENCHMARKING EFFICIENT FIBONACCI ALGORITHMS         ")
    print("==========================================================")

    for n in target_values:
        print(f"\n---> Testing for n = {n}:")

        # Memoized DP (Skipped for 100k due to stack size limits)
        if n <= 1000:
            t_memo = timeit.timeit(lambda: fib_memo(n), number=1)
            print(f" [1] Memoized DP     : Time = {t_memo:.6f} sec")
        else:
            print(f" [1] Memoized DP     : Skipped (Recursion stack limit)")

        # Iterative Tabulation DP
        t_dp = timeit.timeit(lambda: fib_dp(n), number=1)
        print(f" [2] Iterative DP    : Time = {t_dp:.6f} sec")

        # Fast Doubling O(log n)
        t_fast = timeit.timeit(lambda: fib_fast_doubling(n), number=1)
        print(f" [3] Fast Doubling   : Time = {t_fast:.6f} sec")

        # Result digit length tracking
        result = fib_fast_doubling(n)
        print(f" Result has {len(str(result))} total digits.")

    print("\n==========================================================")
    print(f"Sample Output: Fibonacci(100) = {fib_dp(100)}")
    print("==========================================================")