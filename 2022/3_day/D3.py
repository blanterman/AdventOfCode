with open('3_data.txt', 'r') as file:
    data_list = file.readlines()

data_list = [element.strip() for element in data_list]

first_half = [element[:int(len(element)/2)] for element in data_list]
second_half = [element[int(len(element)/2):] for element in data_list]

print(data_list)
print(first_half)
print(second_half)

score = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

total = 0
for i in range(len(first_half)):
    character = "".join(set(first_half[i]) & set(second_half[i]))
    total += score.index(character)

print(total)

total2 = 0
for i in range(0, len(data_list), 3):
    character2 = "".join((set(data_list[i]) & set(data_list[i+1])) & set(data_list[i+2]))
    total2 += score.index(character2)

print(total2)
