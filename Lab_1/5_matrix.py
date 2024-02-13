import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(10**6)

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

#Here I store the results
data = []
execution_times = []
terms=[501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Driver Program
for term in terms:
    start_time = time.time()
    result = fibonacci_matrix(term)
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