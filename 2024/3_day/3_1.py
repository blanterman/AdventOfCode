import re

with open('3_data.txt', 'r') as file:
    lines = file.readlines()

sumMuls = 0
for line in lines:
    validMuls = re.findall("mul\([0-9]+,[0-9]+\)",line)
    for validMul in validMuls:
        nums = re.findall("[0-9]+",validMul)
        sumMuls = sumMuls + (int(nums[0]) * int(nums[1]))
print("Part 1")
print(sumMuls)

with open('3_data.txt', 'r') as file:
    lines = file.readlines()

sumMuls = 0
skip = False
for line in lines:
    mulsDosDonts = re.findall("mul\([0-9]+,[0-9]+\)|do\(\)|don\'t\(\)",line)
    for mulDoDont in mulsDosDonts:
        if not skip:
            if mulDoDont == "don\'t()":
                skip = True
            else:
                nums = re.findall("[0-9]+",mulDoDont)
                try:
                    sumMuls = sumMuls + (int(nums[0]) * int(nums[1]))
                except IndexError:
                    continue
        else:
            if mulDoDont == "do()":
                skip = False
            continue
print("Part 2")
print(sumMuls)
