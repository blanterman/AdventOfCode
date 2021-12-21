
def updateDir (currDir, inst, amnt):
    noChange = ["N", "E", "S", "W", "F"]
    if inst in noChange:
        return currDir
    nextDir = {"L":{"N":{'90':"W", '180':"S", '270':"E"}, "E":{'90':"N", '180':"W", '270':"S"}, "S":{'90':"E", '180':"N", '270':"W"}, "W":{'90':"S", '180':"E", '270':"N"}}, "R":{"N":{'90':"E", '180':"S", '270':"W"}, "E":{'90':"S", '180':"W", '270':"N"}, "S":{'90':"W", '180':"N", '270':"E"}, "W":{'90':"N", '180':"E", '270':"S"}}}
    return nextDir[inst][currDir][amnt]

def updatePos (currDir, instDir, distance):
    if instDir == "L" or instDir == "R":
        return [0, 0]
    if instDir == "F":
        if currDir == "N":
            return [0, distance]
        if currDir == "S":
            return [0, -1 * distance]
        if currDir == "E":
            return [distance, 0]
        if currDir == "W":
            return [-1 * distance, 0]
    if instDir == "N":
        return [0, distance]
    if instDir == "S":
        return [0, -1 * distance]
    if instDir == "E":
        return [distance, 0]
    if instDir == "W":
        return [-1 * distance, 0]

with open('AOC121.dat') as directionData:
    directions = directionData.readlines()
print(directions)
nextAdditions = [0, 0]
current = {"dir":"E", "EW": 0, "NS": 0}
for step in directions:
    dirInst = step[0]
    dirAmnt = step[1:-1]
    nextAdditions = updatePos(current["dir"], dirInst, int(dirAmnt))
    current["dir"] = updateDir(current["dir"], dirInst, dirAmnt)
    current["EW"] = current["EW"] + nextAdditions[0]
    current["NS"] = current["NS"] + nextAdditions[1]
    print(current)

manhattanDistance = abs(current["EW"]) + abs(current["NS"])
print(manhattanDistance)
