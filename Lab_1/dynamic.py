import matplotlib.pyplot as plt
import time
import sys

sys.setrecursionlimit(10**6)

FibArray = [0, 1]
def Fibonacci(n):

	if n < 0:
		print("Incorrect input")
		
	elif n < len(FibArray):
		return FibArray[n]
	else:	 
		FibArray.append(Fibonacci(n - 1) + Fibonacci(n - 2))
		return FibArray[n]

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
    #print(f"Term {term}: Fibonacci({term}) = {result}, Time: {execution_time:.6f} seconds")

#print(data)

plt.plot(terms, execution_times, 'o-', linewidth=0.5)
plt.xlabel('Fibonacci Term')
plt.ylabel('Execution Time (seconds)')
plt.title('Fibonacci Sequence with Execution Time')
plt.show()
