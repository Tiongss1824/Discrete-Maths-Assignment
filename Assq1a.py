import math
from sympy import primerange, primefactors

def smallest_prime_divisor(n):
    """Return the smallest prime divisor of n."""
    for p in primerange(2, int(math.sqrt(n)) + 1):
        if n % p == 0:
            return p
    return n  # n itself is prime

def p_adic_order(n, p):
    """Return the p-adic order α(n) of n."""
    count = 0
    while n % p == 0:
        n //= p
        count += 1
    return count

def f_k(n, k):
    """Calculate f_k(n)."""
    p = smallest_prime_divisor(n)
    alpha = p_adic_order(n, p)
    return (alpha - 1) / (p ** k)

def f_bar_k(k, N):
    """Calculate the average of f_k(n) from n=2 to N."""
    total = 0
    for n in range(2, N + 1):
        total += f_k(n, k)
    return total / N

def infinite_sum_f_bar(N):
    """Calculate the infinite sum of f_bar_k(k)."""
    result = 0
    k = 1
    tolerance = 1e-15  # Small tolerance to stop summation
    while True:
        f_bar = f_bar_k(k, N)
        result += f_bar
        if f_bar < tolerance:
            break
        k += 1
    return result

# Set a large value for N to approximate the limit
N = 10**4  # You can increase this for higher accuracy
result = infinite_sum_f_bar(N)

# Print the result rounded to 12 decimal places
print(f"Sum of f̄_K: {result:.12f}")
