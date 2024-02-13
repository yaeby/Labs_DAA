import decimal
import math
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

sys.setrecursionlimit(10**6)


# 1. Recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


# 2. Memoization (Dynamic Programming) approach
def fibonacci_memoization(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]

    memo[0], memo[1] = 0, 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]


# 3. Iterative approach
def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# 4. Matrix Exponentiation approach
def fibonacci_matrix(n):
    def multiply(matrix1, matrix2):
        return [[matrix1[0][0]*matrix2[0][0] + matrix1[0][1]*matrix2[1][0], matrix1[0][0]*matrix2[0][1] + matrix1[0][1]*matrix2[1][1]],
                [matrix1[1][0]*matrix2[0][0] + matrix1[1][1]*matrix2[1][0], matrix1[1][0]*matrix2[0][1] + matrix1[1][1]*matrix2[1][1]]]

    def power(matrix, n):
        if n <= 1:
            return matrix
        result = power(matrix, n//2)
        result = multiply(result, result)
        if n % 2 == 1:
            result = multiply(result, [[1, 1], [1, 0]])
        return result

    if n == 0:
        return 0
    result_matrix = power([[1, 1], [1, 0]], n-1)
    return result_matrix[0][0]


# 5. Binet's Formula approach
def fibonacci_binet(n):
    decimal.getcontext().prec = 2 * n + 1  # Set precision to handle large numbers

    sqrt_5 = decimal.Decimal(math.sqrt(5))
    phi = (1 + sqrt_5) / 2
    fib_n = ( phi * n - (-1 / phi) * n) / sqrt_5
    return round(fib_n)


# 6. Using Fibonacci sequence properties
def fibonacci_properties(n):
    if n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n+1):
            fib.append(fib[-1] + fib[-2])
        return fib[-1]


# Function to measure elapsed time for a function call
def measure_time(func, n):
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return round(elapsed_time, 6)  # Round the elapsed time to 6 decimal places


# Define the series of Fibonacci terms to be looked up
series_1_raw = np.random.randint(1, 45, size=35)
series_1 = np.sort(series_1_raw)

series_2_raw = np.random.randint(1, 50001, size=40)
series_2 = np.sort(series_2_raw)


func_names = {fibonacci_memoization, fibonacci_iterative, fibonacci_matrix, fibonacci_binet, fibonacci_properties, fibonacci_recursive}
for func in func_names:
    x_values = []
    y_values = []
    if func != fibonacci_recursive:
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
    fig, ax = plt.subplots(figsize=(9, 10.5))
    table_data = np.row_stack((x_values, y_values))  # Combine x and y into a 2D array with rows
    table = ax.table(cellText=table_data.T, colLabels=['n', 'Time (seconds)'], loc='center', cellLoc='left')

    # Set the table formatting
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.2)
    ax.axis('off')
    ax.set_title(f'Table for the {func.__name__} method')

    # Display the table
    plt.show()

    # Plot the graph
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, marker='o')
    plt.xlabel('Fibonacci n-th term')
    plt.ylabel('Time (seconds)')
    plt.title(f'Dependency of Fibonacci n-th term on Time for the {func.__name__} method')
    plt.grid(True)
    plt.show()