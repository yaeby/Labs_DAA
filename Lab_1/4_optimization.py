import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(10**6)

def Fibonacci(n):
	a = 0
	b = 1
	
	if n < 0:
		print("Incorrect input")		
	elif n == 0:
		return 0
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b

#Here I store the results
data = []
execution_times = []
terms=[501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]

# Driver Program
for term in terms:
    start_time = time.time()
    result = Fibonacci(term)
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