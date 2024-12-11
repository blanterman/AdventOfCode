'''
    Checks that the report is valid, which means it is always increasing or 
    decreasing and the difference is no more than +/- 3.
    @param report list of report integers
    @param max_diff integer maximum allowable difference 
    @return 1 if valid, 0 if invalid
'''
def valid(report, max_diff):
    initial_difference = report[1] - report[0]

    if initial_difference == 0:
        return 0

    if initial_difference > 0:
        increase = True
    else:
        increase = False

    if increase:
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff <= 0:
                return 0
            if diff > max_diff:
                return 0

    if not increase:
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff >= 0:
                return 0
            if abs(diff) > max_diff:
                return 0
#    print(report)
    return 1


# Program script
with open('2_data.txt', 'r') as file:
    data_list = file.readlines()
data_list = [list(map(int, element.split())) for element in data_list]
safe_total = 0
max_diff = 3

# Part 1
for report in data_list:
    safe_total = safe_total + valid(report, max_diff)

print("part 1")
print(safe_total)

# Part 2
safe_total = 0
for report in data_list:
    safe = valid(report, max_diff)
    if safe == 1:
        safe_total = safe_total + 1
    else:
        for i in range(len(report)):
            newReport = report[:]
            newReport.pop(i)
            safe = valid(newReport, max_diff)
            if safe == 1:
                safe_total = safe_total + 1
                break

print("part 2")
print(safe_total)
