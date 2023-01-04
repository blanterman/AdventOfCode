"""
    Advent of code 2022 Day 4
    given data that defines a pairs of ranges I need to check each pair of 
    ranges to find if one is contained in the other.

    For part two, I just need to check the pairs of ranges overlap 
"""
# Read the data into a list by line. Each entry in list will look like: '2-4,6-8\n'
with open('4_data.txt', 'r') as file:
    data_list = file.readlines()

# get rid of the trailing \n. Each entry in list will look like '2-4,6-8'
data_list = [element.strip() for element in data_list]
# Make a list of list that seperate the pairs of ranges. 
# Each entry in list will have 2 lists that look like ['2-4', '6-8']
data_lists = [element.split(',') for element in data_list]
# Make a list of lists of lists to seperate the beginning of each range from the end
# Each entry in the list will have 2 entries and each of those entries will have 2 entries
# One entry at the top level will look like [['2', '4'], ['6', '8']]
ranges_data_list = [[entry.split('-') for entry in element] for element in data_lists]

# initialize tracking variables
total = 0
total2 = 0
# go through each element, 
for element in ranges_data_list:
    # create sets using range() and the values in the data
    # using sets allows finding checking subsets, supersets, disjoint etc.
    set1 = set(range(int(element[0][0]),int(element[0][1]) + 1))
    set2 = set(range(int(element[1][0]),int(element[1][1]) + 1))
    print(set1)
    print(set2)
    # Check if subsets of each other for part 1
    if set1.issubset(set2) or set2.issubset(set1):
        total += 1
        print("yes")
    # Check if they aren't disjoint for part 2
    if not set1.isdisjoint(set2):
        total2 += 1
    print()
print(data_list)
print(data_lists)
print(ranges_data_list)
print(total)
print(total2)
