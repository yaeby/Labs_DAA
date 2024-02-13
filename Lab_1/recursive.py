import matplotlib.pyplot as plt
import time

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

#Here I store the results
data = []
execution_times = []
terms=[5, 7, 10, 12, 15, 17, 20,
22, 25, 27, 30, 32, 35, 37, 40, 42, 45]

# Driver Program
for term in terms:
    start_time = time.time()
    result = Fibonacci(term)
    end_time = time.time()
    
    execution_time = end_time - start_time
    execution_times.append(execution_time)
    
    data.append(result)
    print(f"Term {term}: Fibonacci({term}) = {result}, Time: {execution_time:.6f} seconds")

print(data)

plt.plot(terms, execution_times, 'o-', linewidth=0.5)
plt.xlabel('Fibonacci Term')
plt.ylabel('Execution Time (seconds)')
plt.title('Fibonacci Sequence with Execution Time')
plt.show()
