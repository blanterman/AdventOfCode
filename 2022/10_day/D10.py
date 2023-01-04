with open('10_data.txt', 'r') as file:
    operations = file.read().splitlines()

times = [20, 60, 100, 140, 180, 220]
register = 1
cycle_num = 1
total = 0

for operation in operations:
    command = operation[0:4]
    if command == 'addx':
        cycle_num += 1
        if cycle_num in times:
            total += cycle_num * register

        val = int(operation[4:])
        cycle_num += 1
        register += val
        if cycle_num in times:
            total += cycle_num * register
    else:
        cycle_num += 1
        if cycle_num in times:
            total += cycle_num * register
        val = ""

print(total)

register = 1
cycle_num = 1
crt = ""
pixel = 0
for operation in operations:
    line = ""
    command = operation[0:4]
    row = int(pixel/40)
    sprite = range(row * 40 + register - 1, row * 40 + register + 2, 1)
    sprite_norm = range(register - 1, register + 2, 1)
    if command == 'addx':
        if pixel in sprite:
            crt += '#'
        else:
            crt += '.'
        pixel += 1
        if pixel in sprite:
            crt += '#'
        else:
            crt += '.'
        val = int(operation[4:])
        register += val
        pixel += 1
    else:
        if pixel in sprite:
            crt += '#'
        else:
            crt += '.'
        val = ""
        pixel += 1

for i in range(0, len(crt), 40):
    print(str(crt[i:i + 40]))
