import matplotlib.pyplot as plt
import time

def multiply(a, b, x, y):
    return x*(a+b) + a*y, a*x + b*y

def square(a, b):
    a2 = a * a
    b2 = b * b
    ab = a * b
    return a2 + (ab << 1), a2 + b2

def power(a, b, m):
    if m == 0:
        return (0, 1)
    elif m == 1:
        return (a, b)
    else:
        x, y = a, b
        n = 2
        while n <= m:
            # repeated square until n = 2^q > m
            x, y = square(x, y)
            n = n*2
        # add on the remainder
        a, b = power(a, b, m-n//2)
        return multiply(x, y, a, b)

def implicit_fib(n):
    a, b = power(1, 0, n)
    return a

#Here I store the results
data = []
execution_times = []
terms=[1690, 7722, 7748, 11368, 11882, 11896, 13187, 13253, 16463, 16612, 17059, 19320, 20387, 21368, 21829, 22497, 22552, 23433, 23862, 27466, 28146, 29305, 29633, 30559, 30738, 31959, 33083, 33759, 33777, 34125, 34154, 35999, 37750, 39186, 41368, 42446, 44679, 44766, 47612]

# Driver Program
for term in terms:
    start_time = time.time()
    result = implicit_fib(term)
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
