import matplotlib.pyplot as plt
import time

def matrix_multiply(A, B):
    a, b, c, d = A
    x, y, z, w = B
    
    return (
        a*x + b*z,
        a*y + b*w,
        c*x + d*z,
        c*y + d*w,
    )

def matrix_power(A, m):
    if m == 0:
        return [1, 0, 0, 1]
    elif m == 1:
        return A
    else:
        B = A
        n = 2
        while n <= m:
            # repeated square B until n = 2^q > m
            B = matrix_multiply(B, B)
            n = n*2
        # add on the remainder
        R = matrix_power(A, m-n//2)
        return matrix_multiply(B, R)

F1 = [1, 1, 
      1, 0]

def matrix_fib(n):
    return matrix_power(F1, n)[1]

#Here I store the results
data = []
execution_times = []
terms=[501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Driver Program
for term in terms:
    start_time = time.time()
    result = matrix_fib(term)
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
