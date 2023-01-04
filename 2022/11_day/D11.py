with open('11_data_test.txt', 'r') as file:
    lines = file.read().splitlines()

#print(lines)
num_monkeys = int(lines[-6][7])
#print(num_monkeys)
monkeys = {}
names = []
lines.append('')
lines_per_monkey = 7
for i in range(num_monkeys + 1):
    offset = i * lines_per_monkey
    # Monkey Name
    name = lines[offset + 0]
    names.append(name)
    monkeys[name] = {}
    # Item worry level
    items = list(map(int, lines[offset + 1][18:].split(', ')))
    monkeys[name]['items']=items
    # Operation
    operation = lines[offset + 2][19:].split()
    monkeys[name]['operation'] = {'first':operation[0], 'operator':operation[1], 'second':operation[2]}
    # Test
    test = int(lines[offset + 3][21:])
    monkeys[name]['divisor'] = test
    # Next true
    next_true = lines[offset + 4][29:]
    monkeys[name]['next true'] = next_true + ':'
    # Next false
    next_false = lines[offset + 5][30:]
    monkeys[name]['next false'] = next_false + ':'
    # Initiate a count
    monkeys[name]['inspection count'] = 0

for i in range(20):
    for name in names:
        for item in monkeys[name]['items']:
            #first get the new worry level
            new = 0
            first = item
            second = 0
            if monkeys[name]['operation']['second'] == 'old':
                second = item
            else:
                second = int(monkeys[name]['operation']['second'])
            if monkeys[name]['operation']['operator'] == '*':
                new = first * second
            else:
                new = first + second
            #print(new)
            # second update worry level using rule to integer divide by 3
            updated = int(new / 3)
            # Update the count now that the item is inspected
            monkeys[name]['inspection count'] += 1
            #print(updated)
            # test for deciding where to pass
            if updated % monkeys[name]['divisor'] == 0:
                next_monkey_name = 'Monkey ' + monkeys[name]['next true']
            else:
                next_monkey_name = 'Monkey ' + monkeys[name]['next false']
            # pass to the next monkey
            monkeys[next_monkey_name]['items'].append(updated)
        monkeys[name]['items'] = []

counts = []
for name in names:
    counts.append(monkeys[name]['inspection count'])
print(counts)
sorted_counts = sorted(counts, reverse=True)
print(sorted_counts)
print(sorted_counts[0] * sorted_counts[1])

#print(monkeys)
#print(names)

