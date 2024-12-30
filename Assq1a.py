import time, math
start_time = time.time()

def min_prime_factor(n):
    result = [0]*(n+1)
    result[0] = [0,0]
    result[1] = [0,0]
    for x in range(2, n + 1):
        if result[x] == 0:
            for y in range(x, n + 1, x):
                if result[y] == 0:

                    power = 1
                    while y % x**(power +1) == 0:
                        power += 1

                    result[y] = [x, power]
    return result

def estimate(K, number):
    values = min_prime_factor(number)
    total = 0

    for x in range(2, number):
        smallest_prime, p_adic_order = values[x]
        total += (p_adic_order - 1)/(smallest_prime**K)

    return total/number

def list_primality(n):
	result = [True] * (n + 1)
	result[0] = result[1] = False
	for i in range(int(math.sqrt(n)) + 1):
		if result[i]:
			for j in range(2 * i, len(result), i):
				result[j] = False
	return result

def list_primes(n):
	return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]

def f(K):
    primes = list_primes(10**6)
    total = 0
    curr = 1
    for p in primes:
        total += curr*(1/((p**(K+1))*(p-1)))
        curr *= (p - 1)/p
    return round(total, 12)

def sum_f():
    primes = list_primes(10**6)
    total = 0
    curr = 1
    for p in primes:
        total += curr*(1/((p*(p-1)**2)))
        curr *= (p - 1)/p
    return round(total, 12)

if __name__ == "__main__":
    print(sum_f())