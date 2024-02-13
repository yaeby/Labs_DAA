import matplotlib.pyplot as plt
import time
import sys
import decimal
import math

sys.setrecursionlimit(10**6)

def fibonacci_binet(n):
    decimal.getcontext().prec = 2 * n + 1  # Set precision to handle large numbers

    sqrt_5 = decimal.Decimal(math.sqrt(5))
    phi = (1 + sqrt_5) / 2
    fib_n = ( phi * n - (-1 / phi) * n) / sqrt_5
    return round(fib_n)

#Here I store the results
data = []
execution_times = []
terms=[501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Driver Program
for term in terms:
    start_time = time.time()
    result = fibonacci_binet(term)
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