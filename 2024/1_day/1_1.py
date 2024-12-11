# Each data line has two integers seperated by 3 spaces

# Read lines of data into list
with open('1_data.txt', 'r') as file:
    data_list = file.readlines()

#Part 1
# Process data to get a sorted list of the left integers and a sorted list of 
# the right integers on each line.
data_list = [element.split() for element in data_list]
left = sorted([int(element[0]) for element in data_list])
right = sorted([int(element[1]) for element in data_list])
# Compute the sum of the differences of corresponding elements in the left and 
# right lists
sum_of_differences = sum([abs(left[i] - right[i]) for i in range(len(left))])
print(sum_of_differences)

#Part 2
# Compute the sum of an increase score as determined by the prompt
sum_of_increases = sum([element * right.count(element) for element in left])
print(sum_of_increases)
