"""
adventofcode.com 2022
Day 1 part 1
Given a list of caloric value of all the food the elves have, find the maximum
amount of food an elf is carrying.
"""

# Read data into a list and convert the data to integers
with open("1_data.txt", "r") as data:
    data_list = data.read().split("\n\n")

# Clean up the data and get the max sum
# Get rid of all the new line characters at the end of the strings. But keep the
# ones in the middle of the strings
data_list = [element.strip() for element in data_list]

# Each element is a list of calorie count seperated by new line characthers. 
# Seperate the elements into lists. This will return a list of lists. Each list
# of strings that represent calorie count of food.
data_list = [element.split("\n") for element in data_list]

# change all the strings into integers so they can be added together
data_list = [list(map(int, element)) for element in data_list]

# Sum each list in the list of lists to get a list of sums. These elements 
# represent the total calories each elf is carrying.
sums_list = [sum(element_list) for element_list in data_list]

# Find the max value in the list to find how many calories the elf with the 
# Maximum number of calories is carrying.
maximum_sum = max(sums_list)

print("Part 1")
print(data_list)
print(sums_list)
print(maximum_sum)

"""
Day 1 part 2
Find the top three amounts of food that are being carried by the elves and add
them together.
"""
# Sort the list from part 1 (increasing) add the last three elements.
sorted_sums = sorted(sums_list)
sum_top_three = sum(sorted_sums[-3:])

print()
print("Part 2")
print(sorted_sums)
print(sum_top_three)


