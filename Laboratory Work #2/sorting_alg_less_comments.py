from random import randint
from timeit import repeat
from matplotlib import pyplot as plt

'''
Sorting Algorithms:
'''
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False
        if already_sorted:
            break

    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item

    return array

def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    if len(array) < 2:
        return array

    midpoint = len(array) // 2
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

def quick_sort(array):
    if len(array) < 2:
        return array

    low, same, high = [], [], []
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    return quick_sort(low) + same + quick_sort(high)


def heap_sort(array):
    def heapify(array, N, i):
        largest = i  
        l = 2 * i + 1 
        r = 2 * i + 2 

        if l < N and array[largest] < array[l]:
            largest = l
        if r < N and array[largest] < array[r]:
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]  
            heapify(array, N, largest)

    N = len(array)
    for i in range(N // 2 - 1, -1, -1):
        heapify(array, N, i)
    for i in range(N - 1, 0, -1):
        array[i], array[0] = array[0], array[i] 
        heapify(array, i, 0)
    return array

def tim_sort(array):
    def insertion_sort_modified(array, left=0, right=None):
        if right is None:
            right = len(array) - 1
        for i in range(left + 1, right + 1):
            key_item = array[i]
            j = i - 1
            while j >= left and array[j] > key_item:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key_item
        return array
    min_run = 32
    n = len(array)

    for i in range(0, n, min_run):
        insertion_sort_modified(array, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            array[start:start + len(merged_array)] = merged_array

        size *= 2
    return array

'''
Functions to record time and plot data:
'''
def run_sorting_algorithm(algorithm, array):
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    final_time = round(min(times), 6)

    print(f"Algorithm: {algorithm}. Array length: {len(array)}. Minimum execution time: {final_time} sec")
    print("")
    return final_time
    
def plot(times, array_len, algorithm):
    #plot tabel 
    fig, ax = plt.subplots()
    table_data = [[length, time] for length, time in zip(array_len, times)]
    table = ax.table(cellText=table_data, colLabels=['Array Length', 'Time'], loc='center', cellLoc='center')
    ax.set_title(f'Time results of {algorithm} algorithm')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.1, 1.1) 
    ax.axis('off')
    plt.show()

    #plot graph
    plt.plot(array_len, times)
    plt.xlabel("array length")
    plt.ylabel("soring time (s)")
    plt.title(f'{algorithm} algorithm')
    plt.grid('on')
    plt.show()


'''
Empirical Analysis of sorting algorithms
'''
algorithms = ["bubble_sort", "insertion_sort", "merge_sort", "quick_sort", "heap_sort", "tim_sort"]
arrays_lengths = [100, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 15000, 20000, 30000, 40000, 50000, 75000, 100000]
arrays_lengths_2 = [100, 1000, 2000, 3000, 4000, 5000] #array lenghts for bubble & insertion sort only 

if __name__ == "__main__":
    # Creating different size arrays
    arrays = []
    for ARRAY_LENGTH in arrays_lengths:
        array = [randint(-1000, 1000) for j in range(ARRAY_LENGTH)]
        arrays.append(array)

    # Tesing each algorithm with each array created previoslly
    for algorithm in algorithms:
        execution_times = []

        for array in arrays:
            if (len(array) > arrays_lengths_2[-1]) and (algorithm == "bubble_sort" or algorithm == "insertion_sort"): 
                break
            execution_time = run_sorting_algorithm(algorithm=algorithm, array=array)
            execution_times.append(execution_time)

        if algorithm == "bubble_sort" or algorithm == "insertion_sort":
            plot(times=execution_times, array_len=arrays_lengths_2, algorithm=algorithm)
        else:
            plot(times=execution_times, array_len=arrays_lengths, algorithm=algorithm)