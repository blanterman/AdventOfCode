def findStartEnd(contour):
    for i in range(len(contour)):
        for j in range(len(contour[i])):
            if contour[i][j] == 'S':
                start = [i, j]
            if contour[i][j] == 'E':
                end = [i, j]
    return start, end

def value(contour, location):
    if contour[location[0]][location[1]] == 'S':
        return 'a'
    if contour[location[0]][location[1]] == 'E':
        return 'z'
    return contour[location[0]][location[1]]

def Neighbors(x, y):
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        xx = x + dx
        yy = y + dy
        if not (0 <= xx < m and 0 <= yy < n):
            continue
        if 
    neighbors = []
    if location[0] == 0:
        neighbors.append([0, location[1] - 1])
        neighbors.append([1, location[1]])
        neighbors.append([0, location[1] + 1])
        if location[1] == 0:
            neighbors.pop(0)
        if location[1] == len(contour[0]) - 1:
            neighbors.pop()
        return neighbors
    if location[0] == len(contour) - 1:
        neighbors.append([location[0], location[1] - 1])
        neighbors.append([location[0] - 1, location[1]])
        neighbors.append([location[0], location[1] + 1])
        if location[1] == 0:
            neighbors.pop(0)
        if location[1] == len(contour[location[0]]) - 1:
            neighbors.pop()
        return neighbors
    if location[1] == 0:
        neighbors.append([location[0] - 1, 0])
        neighbors.append([location[0], 1])
        neighbors.append([location[0] + 1, 0])
        if location[0] == 0:
            neighbors.pop(0)
        if location[0] == len(contour) - 1:
            neighbors.pop()
        return neighbors
    if location[1] == len(contour[location[0]]) - 1:
        neighbors.append([location[0] - 1, location[1]])
        neighbors.append([location[0], location[1] - 1])
        neighbors.append([location[0] + 1, location[1]])
        if location[0] == 0:
            neighbors.pop(0)
        if location[0] == len(contour) - 1:
            neighbors.pop()
        return neighbors
    neighbors.append([location[0] - 1, location[1]])
    neighbors.append([location[0], location[1] - 1])
    neighbors.append([location[0] + 1, location[1]])
    neighbors.append([location[0], location[1] + 1])
    return neighbors

def processLocation(contour, location, path, paths):
    path.append(location)
    if contour[location[0]][location[1]] == 'E':
        paths.append(len(path) - 1)
        print(paths)
        input("go on to next?")
        path.pop()
        return
    val = value(contour, location)
    neighbors = getNeighbors(contour, location)
    valid_neighbors = []
    for neighbor in neighbors:
        if neighbor not in path:
            valid_neighbors.append(neighbor)
    for valid_neighbor in valid_neighbors:
        if ord(value(contour, valid_neighbor)) - ord(val) <= 1:
            processLocation(contour, valid_neighbor, path, paths)
    path.pop()


with open('12_data.txt', 'r') as file:
    contour = file.read().splitlines()
for line in contour:
    print(line)
start, end = findStartEnd(contour)
path = []
paths = []
"""
for i in range(len(contour)):
    for j in range(len(contour[i])):
        print([i, j], value(contour, [i, j]), getNeighbors(contour, [i, j]))
"""
processLocation(contour, start, path, paths)
print(min(paths))
