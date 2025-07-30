import math
import time

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def is_primes(x):
    if x < 2:
        return False
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(x)) + 1, 6):
        if x % i == 0 or x % (i + 2) == 0:
            return False
    return True


start=time.time()

for x in range(0,10000000):
    is_prime(x)

end=time.time()

print(end-start)