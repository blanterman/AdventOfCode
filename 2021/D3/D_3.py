# Advent of code 2021 day 3

# filters a list of string binary numbers by looking at the first bit location
# in all the entries, seeing if a 1 or 0 is the most common bit value, keeps
# all entries that contain the most common bit in that place number, then moves
# on to the next bit location for the remaining binary numbers. It does this
# recursively until there is only one binary number left in the list.
# @param data_list a list of binary numbers represented by strings.
# @param place_num an integer value representing the current bit location. Not 
#       needed to be supplied, mainly used for recursive call.
def most_common_binary_filter(data_list, place_num=0):
    # Final return for ending recursion when only one binary number left
    if len(data_list) == 1:
        return data_list
    total = 0   # Will add the bits together to see how many 1s 
    most = 0    # Default value of what bit number there is most of
    # Iterate through all the binary numbers in the data_list
    for element in data_list:
        total = total + int(element[place_num]) # Checking how many 1s
    # If half or more than half the entries have a 1, the most occuring number
    # is 1
    if total / len(data_list) >= 0.5:
        most = 1    # most occuring binary digit is 1
    new_list = []   # for all bns with most common digit in current place
    # Go through all entries for qualifying entries
    for element in data_list:
        if int(element[place_num]) == most: # if the digit matches the most
            new_list.append(element)        # common, append to new list
    # Recursive call with new smaller list
    return most_common_binary_filter(new_list, place_num + 1)

# filters a list of string binary numbers by looking at the first bit location
# in all the entries, seeing if a 1 or 0 is the least common bit value, keeps
# all entries that contain the least common bit in that place number, then moves
# on to the next bit location for the remaining binary numbers. It does this
# recursively until there is only one binary number left in the list.
# @param data_list a list of binary numbers represented by strings.
# @param place_num an integer value representing the current bit location. Not 
#       needed to be supplied, mainly used for recursive call.
def least_common_binary_filter(data_list, place_num=0):
    # Final return for ending recursion when only one binary number left
    if len(data_list) == 1:
        return data_list
    total = 0   # Will add the bits together to see how many 1s 
    least = 1    # Default value of what bit number there is least of
    # Iterate through all the binary numbers in the data_list
    for element in data_list:
        total = total + int(element[place_num]) # Checking how many 1s
    # If half or more than half the entries have a 1, the least occuring number
    # is 0
    if total / len(data_list) >= 0.5:
        least = 0    # least occuring binary digit is 1
    new_list = []   # for all bns with least common digit in current place
    # Go through all entries for qualifying entries
    for element in data_list:
        if int(element[place_num]) == least: # if the digit matches the least
            new_list.append(element)        # common, append to new list
    # Recursive call with new smaller list
    return least_common_binary_filter(new_list, place_num + 1)

def bin_list_2_dec(bin_list):
    bin_num = 0
    bit_num = 0
    for bit_pow in range(len(bin_list) - 1, -1, -1):
        bin_num = bin_num + bin_list[bit_num] * pow(2, bit_pow)
        bit_num = bit_num + 1
    return bin_num

# Day 3 part 1
# Reading in some binary data to extract information

# Read data into a list and clean up the data
with open("3_1.txt", "r") as data:
    data_list = data.read().split("\n")
# Figuring out which binary value is most and least common in each bit location
# through out the entire list, then make a binary number out of those most and 
# least common values, change from binary to decimal and multiply.
total = 0   # Used to keep track of the number of 1s in the current bit location
list_length = len(data_list)
most = 0    # Default value of the most occuring binary value
gamma_bits = []     # Gamma is for most occuring, epsilon is for least
# go through each bit location from msb to lsb
for place_num in range(len(data_list[0])):
    # check each binary number at current location and add 1s together
    for item in data_list:
        total = total + int(item[place_num])
    # if more than half the values are ones we know 1s are the most
    if total / list_length > 0.5:
        most = 1
    # Append the value for this bit location to the list
    gamma_bits.append(most)
    # Reset the working variables
    most = 0
    total = 0
# epsilon bits are just the inverse of the gamma bits
epsilon_bits = [0 if val == 1 else 1 for val in gamma_bits]
# Convert the binary digits to decimal, multiply them to get answer
g_bin_num = bin_list_2_dec(gamma_bits)
e_bin_num = bin_list_2_dec(epsilon_bits)
print("gamma value = {}, epsilon value = {}".format(g_bin_num, e_bin_num))
print("Product of gamma and epsilon: {}".format(g_bin_num * e_bin_num))

# Day 3 Part 2
# Extract more information about the binary data using functions above

# Apply the most common binary digit filter to get Oxygen Generation Statistic
o2gen = most_common_binary_filter(data_list)
# Convert the string binary value to a list of binary 1s and 0s
o2gen_bits = [1 if char == '1' else 0 for word in o2gen for char in word]
# Apply the least common binary digit filter to get Carbon Dioxide Purge stat.
co2prg = least_common_binary_filter(data_list)
# Convert the string binary value to a list of binary 1s and 0s
co2prg_bits = [1 if char == '1' else 0 for word in co2prg for char in word]
# Convert the binary digit list to decimal value then multiply them for answer
o2gen_dec = bin_list_2_dec(o2gen_bits)
co2prg_dec = bin_list_2_dec(co2prg_bits)
print("Oxygen Generation Stat: {}. Carbon Dioxide Purge Stat: {}.".format(o2gen_dec, co2prg_dec))
print("Product of O2Gen and CO2Purge: {}.".format(o2gen_dec * co2prg_dec))
