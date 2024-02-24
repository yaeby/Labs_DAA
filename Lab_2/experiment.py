import matplotlib.pyplot as plt

# Assuming time is a 2D array and array_len is a 1D array
# Replace the following with your actual data
time = [[1, 2, 3, 4, 5],  # replace with your data
        [6, 7, 8, 9, 10],  # replace with your data
        [11, 12, 13, 14, 15]]  # replace with your data

array_len = [10, 20, 30, 40, 50]  # replace with your data

# Take the first row of time and plot against array_len
first_row_of_time = time[0]

# plt.plot(array_len, first_row_of_time, label='First Row of Time')
# plt.xlabel('Array Length')
# plt.ylabel('Values from First Row of Time')
# plt.title('Plotting First Row of Time against Array Length')
# plt.legend()
# plt.show()

# print(time[0])
# print(time[1])
# print(time[2][4])
# print(time)

# # Create an empty 2D array
# two_d_array = []

# # Append data to the first row
# row1_data = [1, 2, 3]
# two_d_array.append(row1_data)

# # Append data to the second row
# row2_data = [4, 5, 6]
# two_d_array.append(row2_data)

# # Append data to the third row
# row3_data = [7, 8, 9]
# two_d_array.append(row3_data)

# # Print the resulting 2D array
# print(two_d_array)

# Create an empty 2D array
two_d_array = []

# Assuming you have a function that returns an integer
def your_function():
    # Replace this with your actual function logic
    import random
    return random.randint(1, 100)

# Number of rows in the 2D array
num_rows = 3

# Number of times to call the function (you can adjust this as needed)
num_iterations = 6

# Loop to populate the 2D array
for i in range(num_iterations):
    # Call the function to get a value
    value = your_function()
    print(value)
    # Check if the 2D array has enough rows, if not, add a new row
    if len(two_d_array) < num_rows:
        two_d_array.append([value])
    else:
        # If there are enough rows, append the value to the appropriate row
        two_d_array[i % num_rows].append(value)

# Print the resulting 2D array
for row in two_d_array:
    print(row)

print(two_d_array)