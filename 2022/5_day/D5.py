"""

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

[M]                     [N] [Z]    
[F]             [R] [Z] [C] [C]    
[C]     [V]     [L] [N] [G] [V]    
[W]     [L]     [T] [H] [V] [F] [H]
[T]     [T] [W] [F] [B] [P] [J] [L]
[D] [L] [H] [J] [C] [G] [S] [R] [M]
[L] [B] [C] [P] [S] [D] [M] [Q] [P]
[B] [N] [J] [S] [Z] [W] [F] [W] [R]
 1   2   3   4   5   6   7   8   9 

"""

with open('5_data.txt', 'r') as file:
    data_list = file.read().splitlines()

instructions = [element.split() for element in data_list]

for instruction in instructions:
    instruction[1] = int(instruction[1])
    instruction[3] = int(instruction[3])
    instruction[5] = int(instruction[5])
"""
piles = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
piles2 = [['Z', 'N'], ['M', 'C', 'D'], ['P']]
"""
piles = [['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'], \
         ['N', 'B', 'L'], \
         ['J', 'C', 'H', 'T', 'L', 'V'], \
         ['S', 'P', 'J', 'W'], \
         ['Z', 'S', 'C', 'F', 'T', 'L', 'R'], \
         ['W', 'D', 'G', 'B', 'H', 'N', 'Z'], \
         ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'], \
         ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'], \
         ['R', 'P', 'M', 'L', 'H']]
piles2 = [['B', 'L', 'D', 'T', 'W', 'C', 'F', 'M'], \
         ['N', 'B', 'L'], \
         ['J', 'C', 'H', 'T', 'L', 'V'], \
         ['S', 'P', 'J', 'W'], \
         ['Z', 'S', 'C', 'F', 'T', 'L', 'R'], \
         ['W', 'D', 'G', 'B', 'H', 'N', 'Z'], \
         ['F', 'M', 'S', 'P', 'V', 'G', 'C', 'N'], \
         ['W', 'Q', 'R', 'J', 'F', 'V', 'C', 'Z'], \
         ['R', 'P', 'M', 'L', 'H']]

for instruction in instructions:
    source = instruction[3] - 1
    destination = instruction[5] - 1
    count = instruction[1]
    for i in range(count):
        piles[destination].append(piles[source].pop())

answer = ''
for pile in piles:
    answer += pile[len(pile) - 1]

print(piles)
print(answer)

for instruction in instructions:
    temp_pile = []
    source = instruction[3] - 1
    destination = instruction[5] - 1
    count = instruction[1]
    for i in range(count):
        temp_pile.append(piles2[source].pop())
    for i in range(len(temp_pile)):
        piles2[destination].append(temp_pile.pop())

answer2 = ''
for pile in piles2:
    answer2 += pile[len(pile) - 1]
print(piles2)
print(answer2)
