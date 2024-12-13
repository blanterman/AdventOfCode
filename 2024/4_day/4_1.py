with open('4_data.txt', 'r') as file:
    dataLines = file.readlines()

dataLines = [element.strip() for element in dataLines]

word = 'XMAS'
wordAsList = list(word)
xmasCount = 0
potWord = []

# right
for m in range(len(dataLines)):
    for n in range(len(dataLines[m])-3):
        potWord = [dataLines[m][n], dataLines[m][n+1], dataLines[m][n+2], dataLines[m][n+3]]
        if potWord == wordAsList:
            xmasCount = xmasCount + 1
# left
for m in range(len(dataLines)):
    for n in range(3, len(dataLines[m])):
        potWord = [dataLines[m][n], dataLines[m][n-1], dataLines[m][n-2], dataLines[m][n-3]]
        if potWord == wordAsList:
            xmasCount = xmasCount + 1
# down
for m in range(len(dataLines) - 3):
    for n in range(len(dataLines[m])):
        potWord = [dataLines[m][n], dataLines[m+1][n], dataLines[m+2][n], dataLines[m+3][n]]
        if potWord == wordAsList:
            xmasCount = xmasCount + 1
# up
for m in range(3, len(dataLines)):
    for n in range(len(dataLines[m])):
        potWord = [dataLines[m][n], dataLines[m-1][n], dataLines[m-2][n], dataLines[m-3][n]]
        if potWord == wordAsList:
            xmasCount = xmasCount + 1
# down left
for m in range(len(dataLines) - 3):
    for n in range(3, len(dataLines[m])):
        potWord = [dataLines[m][n], dataLines[m+1][n-1], dataLines[m+2][n-2], dataLines[m+3][n-3]]
        if potWord == wordAsList:
            xmasCount = xmasCount + 1
# up right
for m in range(3, len(dataLines)):
    for n in range(len(dataLines[m])-3):
        potWord = [dataLines[m][n], dataLines[m-1][n+1], dataLines[m-2][n+2], dataLines[m-3][n+3]]
        if potWord == wordAsList:
            xmasCount = xmasCount + 1
# down right
for m in range(len(dataLines) - 3):
    for n in range(len(dataLines[m]) - 3):
        potWord = [dataLines[m][n], dataLines[m+1][n+1], dataLines[m+2][n+2], dataLines[m+3][n+3]]
        if potWord == wordAsList:
            xmasCount = xmasCount + 1
# up left
for m in range(3, len(dataLines)):
    for n in range(3, len(dataLines[m])):
        potWord = [dataLines[m][n], dataLines[m-1][n-1], dataLines[m-2][n-2], dataLines[m-3][n-3]]
        if potWord == wordAsList:
            xmasCount = xmasCount + 1
print("Part 1")
print(xmasCount)
# try 1 2459 Low
# try 2 2464 correct

#Part 2
xmasCount = 0
validCorners = [['M', 'S', 'M', 'S'], ['M', 'M', 'S', 'S'], ['S', 'M', 'S', 'M'], ['S', 'S', 'M', 'M']]
for m in range(1, len(dataLines)-1):
    for n in range(1, len(dataLines[m])-1):
        if dataLines[m][n] == 'A':
            corners = [dataLines[m-1][n-1], dataLines[m-1][n+1], dataLines[m+1][n-1], dataLines[m+1][n+1]]
            if corners in validCorners:
                xmasCount = xmasCount + 1
print("Part 2")
print(xmasCount)
