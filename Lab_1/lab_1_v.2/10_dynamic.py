import matplotlib.pyplot as plt
import time
from functools import lru_cache
from gmpy2 import mpz


def multiply(a, b, x, y):
    return x*(a+b) + a*y, a*x + b*y

def square(a, b):
    a2 = a * a
    b2 = b * b
    ab = a * b
    return a2 + (ab << 1), a2 + b2

@lru_cache(100)
def dynamic_repeated_squares(a, b, n):
    # n must be a power of two. 
    if n == 0:
        return (0, 1)
    elif n == 1:
        return (a, b)
    return square(*dynamic_repeated_squares(a, b, n//2))
    
def dynamic_power(a, b, m):
    if m == 0:
        return (0, 1)
    elif m == 1:
        return (a, b)
    else:
        # hit the cache for powers of 2
        n = 2
        while n <= m:
            n = n*2
        n = n // 2
        x, y = dynamic_repeated_squares(a, b, n)

        # add on the remainder
        a, b = dynamic_power(a, b, m-n)
        return multiply(x, y, a, b)
    
def dynamic_fib(n):
    a, b = dynamic_power(mpz(1), mpz(0), mpz(n))
    return a

#Here I store the results
data = []
execution_times = []
terms=[501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Driver Program
for term in terms:
    start_time = time.time()
    result = dynamic_fib(term)
    end_time = time.time()
    
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    
    data.append(result)
    print(f"Fibonacci({term}): {execution_time:.6f} seconds")

plt.plot(terms, execution_times, 'o-', linewidth=0.5)
plt.xlabel('Fibonacci Term')
plt.ylabel('Execution Time (seconds)')
plt.title('Fibonacci Sequence with Execution Time')
plt.show()
