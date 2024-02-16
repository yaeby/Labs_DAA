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

def naive_matrix_power(A, m):
    if m == 0:
        return [1, 0, 0, 1]
    B = A
    for _ in range(m-1):
        B = matrix_multiply(B, A)
    return B

F1 = [1, 1, 
      1, 0]

def naive_matrix_fib(n):
    return naive_matrix_power(F1, n)[1]


#Here I store the results
data = []
execution_times = []
terms=[501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Driver Program
for term in terms:
    start_time = time.time()
    result = naive_matrix_fib(term)
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
