# Advent of code 2021 day 1 part 1
# a list of depth values is given
# need to see how many of the values are greater than the previous value

# Read data into a list and convert the data to integers
with open("1_1.txt", "r") as data:
    data_list = data.read().split("\n")
data_list = list(map(int, data_list))

# Instantiate the total number of values that are greater than previous values
total = 0
# Go through the list comparing next value to the current one to see if 
# it is greater. If it is, then we add one to the total.
for index in range(len(data_list) - 1):
    if data_list[index + 1] > data_list[index]:
        total = total + 1
print(total)

# Advent of code 2021 day 1 part 2
# Using same list above do the same thing, but with successive overlapping 
# groups of three elements of the list.
total2 = 0
for index in range(len(data_list) - 3):
    current_group_total = data_list[index] + data_list[index + 1] + data_list[index + 2]
    next_group_total = data_list[index + 1] + data_list[index + 2] + data_list[index + 3]
    if next_group_total > current_group_total:
        total2 = total2 + 1
print(total2)
