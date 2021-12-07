# Advent of code 2021 day 2 part 1
# This question gives you data of movement commands that need to be interpreted
# to update position values.

# Day 2 part 1
# Read data into a list and clean up the data
with open("2_1.txt", "r") as data:
    data_list = data.read().split("\n")
#data_list = list(map(int, data_list))
#print(data_list)
data_list = [item.split(" ") for item in data_list]
#print(data_list)
data_list = [[item[0], int(item[1])] for item in data_list]
#print(data_list)
# Instantiate the beginning values of position [horizontal, depth]
position = [0, 0]

# Go through the commands decoding the instruction and updating the position.
for item in data_list:
    command = item[0]
    ammount = item[1]
    if command == "forward":
        position[0] = position[0] + ammount
    if command == "down":
        position[1] = position[1] + ammount
    if command == "up":
        position[1] = position[1] - ammount

print("Your final position [horizontal, depth] is {}.".format(position))
print("Your horizontal postion multiplied by your depth is {}.".format(position[0] * position[1]))


# Day 2 part 2
# Instantiate the beginning values of position [horizontal, depth, aim]
position = [0, 0, 0]

# Go through the commands decoding the instruction and updating the position.
for item in data_list:
    command = item[0]
    ammount = item[1]
    if command == "down":
        position[2] = position[2] + ammount
    if command == "up":
        position[2] = position[2] - ammount
    if command == "forward":
        position[0] = position[0] + ammount
        position[1] = position[1] + position[2] * ammount

print("Your final position [horizontal, depth, aim] is {}.".format(position))
print("Your horizontal postion multiplied by your depth is {}.".format(position[0] * position[1]))
