
def dir_value(ind, dir_dirs, dir_files):
    value = 0
    if dir_dirs[ind + 1] == []:
        for file in dir_files[ind + 1]:
            size = int(file.split()[0])
            #print(size)
            value += size
        return value
    else:
        for file in dir_files[ind + 1]:
            size = int(file.split()[0])
            #print(size)
            value += size
        for sub_dir in dir_dirs[ind + 1]:
            value += dir_value(dir_dirs.index(sub_dir, ind), dir_dirs, dir_files)
    return value



with open('7_data.txt', 'r') as file:
    terminal_data = file.read().splitlines()
#print(terminal_data)

dir_files = []
dir_dirs = []
total_size = 0
i = 0
cur_dir = ''
ind1 = 0
ind2 = 0
while i < len(terminal_data):
    entry_items = terminal_data[i].split()
    if entry_items[0] == '$':
        if entry_items[1] == 'cd':
            if entry_items[2] != '..':
                cur_dir = entry_items[2]
                dir_dirs.append(cur_dir)
                ind1 += 1
                dir_dirs.append([])
                ind1 += 1
                dir_files.append(cur_dir)
                ind2 += 1
                dir_files.append([])
                ind2 += 1
    elif entry_items[0] == 'dir':
        dir_dirs[ind1 - 1].append(entry_items[1])
    else:
        dir_files[ind2 - 1].append(" ".join(entry_items))
        size = int(entry_items[0])
        total_size += size
    i += 1


print()
print(dir_dirs)
print()
print(dir_files)
totals = []
total = 0
for i in range(0, len(dir_dirs), 2):
    temp = []
    size_dir = dir_value(i, dir_dirs, dir_files)
    print("Directory {} has the size: {}.".format(dir_dirs[i], size_dir))
    temp.append(dir_dirs[i])
    temp.append(size_dir)
    totals.append(temp)
    if size_dir <= 100000:
        print(dir_dirs[i])
        total += size_dir
print()
print(total)

# Part 2
print("\n\n\n\n\n\n")
print(totals)
total_space = 70000000
needed_space = 30000000
available_space = total_space - total_size
print("currently you have {} of available space.".format(available_space))
still_needed = needed_space - available_space
print(still_needed)
minimum = total_space
for element in totals:
    if element[1] >= still_needed:
        if element[1] < minimum:
            minimum = element[1]
print(minimum)
