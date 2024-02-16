import decimal
import math
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(10**6)

'''
Fibonacci functions
'''

# 1. Recursive approach
def recusive_fib(n):
    if n <= 1:
        return n
    else:
        return recusive_fib(n-1) + recusive_fib(n-2)


# 2. Dynamic Programming approach (with memoization)
def dynamic_fib(n, storage=None):
    if storage is None:
        storage = {}
    if n in storage:
        return storage[n]

    storage[0], storage[1] = 0, 1
    for i in range(2, n + 1):
        storage[i] = storage[i - 1] + storage[i - 2]
    return storage[n]


# 3. Tabular approach
def table_fib(n):
    if n < 2:
        return n
    table = [-1] * (n+1)
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]


# 4. Iterative approach
def iterative_fib(n):
    previous, current = (0, 1)
    for i in range(2, n+1):
        previous, current = (current, previous + current)
    return current


# 5. Fibonacci sequence properties approach
def properties_fib(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]


# 6. Eigenvalue approach
def eigen_fib(n, mod=10**9 + 7):
    def mod_pow(base, exp, mod):
        result = 1
        base = base % mod
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            exp = exp // 2
            base = (base * base) % mod
        return result

    F1 = np.array([[1, 1], [1, 0]])
    eigenvalues, eigenvectors = np.linalg.eig(F1)
    
    # Use modular exponentiation to prevent overflow
    Fn = eigenvectors @ np.diag([mod_pow(eig, n, mod) for eig in eigenvalues]) @ eigenvectors.T
    
    return int(np.rint(Fn[0, 1])) % mod


# 7. Matrix approach
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

def matrix_fib(n):
    a, b = power(1, 0, n)
    return a

    
# 8. Binet's Formula approach
def binet_fib(n):
    decimal.getcontext().prec = 2 * n + 1  # Set precision to handle large numbers

    sqrt_5 = decimal.Decimal(math.sqrt(5))
    phi = (1 + sqrt_5) / 2
    fib_n = ( phi * n - (-1 / phi) * n) / sqrt_5
    return round(fib_n)


'''
Recordings
'''
# Function to measure elapsed time for a function call
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return round(elapsed_time, 6)  # Round the elapsed time to 6 decimal places


# Define the series of Fibonacci terms to be looked up
series_1_raw = np.random.randint(1, 45, size=1)
series_1 = np.sort(series_1_raw)

series_2_raw = np.random.randint(1, 50001, size=40)
series_2 = np.sort(series_2_raw)


func_names = [recusive_fib, dynamic_fib, table_fib, iterative_fib, properties_fib, eigen_fib, matrix_fib, binet_fib]
for func in func_names:
    x_values = []
    y_values = []
    if func != recusive_fib:
        for n in series_2:
            elapsed_time = measure_time(func, int(n))
            x_values.append(n)
            y_values.append(elapsed_time)
    else:
        for n in series_1:
            elapsed_time = measure_time(func, int(n))
            x_values.append(n)
            y_values.append(elapsed_time)

    # Create the table
    fig, ax = plt.subplots(figsize=(6, 9))
    table_data = np.row_stack((x_values, y_values))  # Combine x and y into a 2D array with rows
    table = ax.table(cellText=table_data.T, colLabels=['n-th Fibonacci termen', 'Time (s)'], loc='center', cellLoc='left')

    # Set the table formatting
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1)
    ax.axis('off')
    ax.set_title(f'Time result of {func.__name__} function')

    # Display the table
    plt.show()

    # Plot the graph
    plt.figure(figsize=(9, 6))
    plt.plot(x_values, y_values, 'o-')
    plt.xlabel('n-th Fibonacci Term')
    plt.ylabel('Time (s)')
    plt.title(f'{func.__name__} function')
    plt.show()