from random import randint
from timeit import repeat
from matplotlib import pyplot as plt

'''
Sorting Algorithms:
'''
def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0

    # Now go through both arrays until all the elements
    # make it into the resultant array
    while len(result) < len(left) + len(right):
        # The elements need to be sorted to add them to the
        # resultant array, so you need to decide whether to get
        # the next element from the first or the second array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))

def quick_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quick_sort(low) + same + quick_sort(high)


def heap_sort(array):
    def heapify(array, N, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < N and array[largest] < array[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < N and array[largest] < array[r]:
            largest = r

        # Change root, if needed
        if largest != i:
            array[i], array[largest] = array[largest], array[i]  # swap

            # Heapify the root.
            heapify(array, N, largest)

    N = len(array)
    # Build a maxheap.
    for i in range(N // 2 - 1, -1, -1):
        heapify(array, N, i)
    # One by one extract elements
    for i in range(N - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # swap
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

    # Start by slicing and sorting small portions of the
    # input array. The size of these slices is defined by
    # your `min_run` size.
    for i in range(0, n, min_run):
        insertion_sort_modified(array, i, min((i + min_run - 1), n - 1))

    # Now you can start merging the sorted slices.
    # Start from `min_run`, doubling the size on
    # each iteration until you surpass the length of
    # the array.
    size = min_run
    while size < n:
        # Determine the arrays that will
        # be merged together
        for start in range(0, n, size * 2):
            # Compute the `midpoint` (where the first array ends
            # and the second starts) and the `endpoint` (where
            # the second array ends)
            midpoint = start + size - 1
            end = min((start + size * 2 - 1), (n-1))

            # Merge the two subarrays.
            # The `left` array should go from `start` to
            # `midpoint + 1`, while the `right` array should
            # go from `midpoint + 1` to `end + 1`.
            merged_array = merge(
                left=array[start:midpoint + 1],
                right=array[midpoint + 1:end + 1])

            # Finally, put the merged array back into
            # your array
            array[start:start + len(merged_array)] = merged_array

        # Each iteration should double the size of your arrays
        size *= 2
    return array

'''
Functions to record time and plot data:
'''
def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    final_time = round(min(times), 6)

    print(f"Algorithm: {algorithm}. Array lenght: {len(array)}. Minimum execution time: {final_time} sec")
    print("")
    return final_time
    
def plot(times, array_len, algorithm):
    fig, ax = plt.subplots()
    table_data = [[length, time] for length, time in zip(array_len, times)]
    table = ax.table(cellText=table_data, colLabels=['Array Length', 'Time'], loc='center', cellLoc='center')
    ax.set_title(f'Time results of {algorithm} algorithm')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.1, 1.1) 
    ax.axis('off')
    plt.show()

    plt.plot(array_len, times)
    plt.xlabel("array lenght")
    plt.ylabel("soring time (s)")
    plt.title(f'{algorithm} algorithm')
    plt.grid('on')
    plt.show()


'''
Emperical Analysis of sorting algorithms
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
