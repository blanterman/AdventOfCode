# Open the file and read in the data
with open('5_data.txt', 'r') as file:
    data = file.read()

# Seperate the rules from the updates
rulesList, updates = data.split('\n\n')

# Get a list of the individual rules
instructions = rulesList.split('\n')

# Get a list of the updates and clean up a bit.
updateList = updates.split('\n')
updateList = updateList[:-1]

'''
    Function for verifying if an update follows the rules given

    @param dictionary of rules
    @param list of update entries that can be valid or invalid
    @return valid, location valid is a bool, location is list of two values
        that indicate which two locations dont follow the rules in relation
        to eachother.
'''
def verify(rules,entries):
    for i in range(len(entries)-1):
        for j in range(i+1, len(entries)):
            try:
                if entries[i] not in rules[entries[j]]:
                    return False, [i,j]
            except KeyError:
                return False, [i,j]
    return True, [i,j]

# Put the rules list into a dictionary where the rules are organized thusly:
# Keys are elements that can have elements before them
# Value is the list of elements that must appear before the key value
rules = {}
for instruction in instructions:
    before, after = instruction.split('|')
    try:
        rules[after].append(before)
    except KeyError:
        rules[after] = [before]

validUpdates = []
invalidUpdates = []
problemLocation = []
# go through the updates and see which ones are valid. Put valid and invalid
# updates in seperate lists
for update in updateList:
    entries = update.split(',')
    valid, problemLocation = verify(rules, entries)
    if valid:
        validUpdates.append(entries)
    else:
        invalidUpdates.append(entries)

# Add the center elements of the valid updates to get the answer requested
sumOfCenters = 0
for validUpdate in validUpdates:
    sumOfCenters = sumOfCenters + int(validUpdate[len(validUpdate)//2])
print("Part 1")
print(sumOfCenters)

newValids = []
# Go through the invalid updates and validate them by swapping elements that
# are causing the validation to fail
for entries in invalidUpdates:
    valid = False
    while not valid:
        valid, problemLocation = verify(rules, entries)
        if valid:
            newValids.append(entries)
        else:
            temp = entries[problemLocation[0]]
            entries[problemLocation[0]] = entries[problemLocation[1]]
            entries[problemLocation[1]] = temp

# Add the center elements of the newly valid updates to get the answer requested
sumOfCenters = 0
for validUpdate in newValids:
    sumOfCenters = sumOfCenters + int(validUpdate[len(validUpdate)//2])
print("Part 2")
print(sumOfCenters)
# try 1 4870 too low
# try 2 4922 correct
