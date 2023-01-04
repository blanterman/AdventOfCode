def process_daily_timers_better(timers):
    # make the number of zeros the number of nines, which is zero at this 
    # point. These will become the number of eights after the pop
    timers[9] = timers[0]
    # add the number of zeros to the number of sevens because zeros change to 
    # sixes and the sevens will be sixes after the pop
    timers[7] = timers[7] + timers[0]
    # Now that we have used the zeros where needed, pop them off. This 
    # effectively decreses the value of all the timers.
    timers.pop(0)
    # Add a zero back on to the end for the next itteration.
    timers.append(0)
    return timers

def process_daily_timers(timers):
    # initialize the number of eights to be added on to the end of the list
    eights = 0
    # Parse the list, if ithe number is a 0, we will append an eight to the end
    # of the list at the end, and it starts over at 6. Otherwise decrease the 
    # number. Add all the eights on at the end of the analysis
    for i in range(len(timers)):
        if timers[i] == 0:
            eights = eights + 1
            timers[i] = 6
        else:
            timers[i] = timers[i] - 1
    timers += eights * [8]
    return timers

# Get the data line from the file
with open("6_1.txt", "r") as data:
    data_list = data.read().splitlines()
# Create a list of strings split on the comma
timers_str = data_list[0].split(",")
# Convert the strings into integers
timers = list(map(int, timers_str))

# initial processing
# find the maximum value in the original list
maxVal = max(timers)
# initialized the list of counts of values. The index here represents the value
# that is being counted. This means that the value in index zero represents the
# number of zeros in the original list. We will only count the elements once.
timersCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# count the elements up to the max value and put in the list according to its
# index
for i in range(maxVal + 1):
    timersCount[i] = timers.count(i)

# initialize the number of days to update the count list.
num_days = 256
# update the count list 
for i in range(num_days):
    print("Processing day {}.".format(i + 1))
    timersCount = process_daily_timers_better(timersCount)
    #timers = process_daily_timers(timers)
print("There are {} fish after {} days.".format(sum(timersCount), num_days))
