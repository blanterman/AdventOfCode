
def get_max (routes):
    max_route = 0
    index_max = 0
    for route in routes:
        if route != 'x':
            if int(route) > max_route:
                max_route = int(route)
                index_max = routes.index(route)
    return max_route, index_max

def get_relation(max_route, route):
    print("call")
    ind_diff = max_route[1] - route[1]
    found = False
    index = 1
    value = 0
    while (not found):
        value = max_route[0] * index
        if (value - ind_diff) % route[0] != 0:
            index = index + 1
        else:
            print("success")
            found = True
    return index


with open('AOC131.dat') as busInfo:
    lines = busInfo.readlines()
print(lines)
time = int(lines[0][:-1])
routes = lines[1].split(',')
print(time)
print(routes)
minWaitTime = time
currentAnswer = 0
values_and_indeces = []
for route in routes:
    if route != 'x':
        values_and_indeces.append([int(route), routes.index(route)])
        waitTime = int(route) - (time % int(route))
        if waitTime < minWaitTime:
            minWaitTime = waitTime
            currentAnswer = int(route) * waitTime
            print('Route {}: {} minutes, Answer Here: {}'.format(route, minWaitTime, currentAnswer))

max_route, index_max = get_max(routes)
print(max_route)
print(index_max)
print(values_and_indeces)
relations = []
max_route_l = [max_route, index_max]
for pair in values_and_indeces:
    to_add = [pair[0], get_relation(max_route_l, pair)]
    if pair[0] != max_route_l[0]:
        relations.append(to_add)
print(relations)
#current = relations[0]
#for x in range(1, len(relations)):
#    temp = [current[0] * relations[x][0], current[0] * relations[x][1] + current[1]]
#    current = temp
current = relations[0]
curr_equation = [current[0], 0]
next_equation = []
for x in range(1, len(relations)):
    finding = True
    test_val = 1
    while finding:
        if (relations[x][0] * test_val + relations[x][1] - current[0] * curr_equation[1] - current[1]) % curr_equation[0] == 0:
            next_equation = [curr_equation[0] * relations[x][0], test_val]
            finding = False
            print(next_equation)
        else:
            test_val = test_val + 1
    curr_equation = next_equation
    current = relations[x]
print(curr_equation)
final_index = curr_equation[1] * relations[-1][0] + relations[-1][1]
final_answer = final_index * max_route - (index_max - values_and_indeces[0][1])
print("The first occurence is {}".format(final_answer))
#timestamp = 0
#x_val = 0
#testing = True
#earliest = 0
#while(testing):
#    timestamp = max_route * x_val
##    print(timestamp)
#    for pair in values_and_indeces:
#        diff = index_max - pair[1]
#        if (timestamp - diff) % pair[0] != 0:
#            x_val = x_val + 1
#            break
#        if pair[1] == values_and_indeces[-1][1]:
#            testing = False
#            earliest = timestamp - (index_max - values_and_indeces[0][1])
#            print("The earliest time stamp is {}.".format(earliest))

print("test complete")

