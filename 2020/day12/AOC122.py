
def updateWayPoint (waypoint, inst, amnt):
    if inst == "F":
        return waypoint
    if inst == "N":
        return [waypoint[0], waypoint[1] + amnt]
    if inst == "E":
        return [waypoint[0] + amnt, waypoint[1]]
    if inst == "S":
        return [waypoint[0], waypoint[1] - amnt]
    if inst == "W":
        return [waypoint[0] - amnt, waypoint[1]]
    rotations = int(amnt / 90)
    if inst == "L":
        for num in range(rotations):
            waypoint = [-1 * waypoint[1], waypoint[0]]
    if inst == "R":
        for num in range(rotations):
            waypoint = [waypoint[1], -1 * waypoint[0]]
    return waypoint

def updatePos (waypoint, current, numTimes, dirInst):
    if dirInst != "F":
        return current
    return [current[0] + numTimes * waypoint[0], current[1] + numTimes * waypoint[1]]

with open('AOC121.dat') as directionData:
    directions = directionData.readlines()

print(directions)

nextAdditions = [0, 0]
waypoint = [10, 1]
current = [0, 0]

for step in directions:
    dirInst = step[0]
    dirAmnt = int(step[1:-1])
    waypoint = updateWayPoint(waypoint, dirInst, dirAmnt)
    current = updatePos(waypoint, current, dirAmnt, dirInst)
    print(current)
    print(waypoint)
    print("")

manhattanDistance = abs(current[0]) + abs(current[1])
print(manhattanDistance)

