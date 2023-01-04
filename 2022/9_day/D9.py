class Knot:
    def __init__(self, start_x, start_y):
        self.x = start_x
        self.y = start_y
        self.history = [(start_x, start_y)]
    def updatePosition(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.history.append((new_x, new_y))
    def getPosition(self):
        return self.x, self.y
    def getHistory(self):
        return self.history

class Board:

    def __init__(self, list_of_knots):
        self.knots = list_of_knots

    def move_next(self, leader, follower):
        leader_x, leader_y = self.knots[leader].getPosition()
        follower_x, follower_y = self.knots[follower].getPosition()
        if (abs(leader_x - follower_x) < 2) and (abs(leader_y - follower_y) < 2):
            self.knots[follower].updatePosition(follower_x, follower_y)
            return
        # right
        if (leader_x - follower_x == 2) and (leader_y == follower_y):
            self.knots[follower].updatePosition(follower_x + 1, follower_y)
            return
        # left
        if (leader_x - follower_x == -2) and (leader_y == follower_y):
            self.knots[follower].updatePosition(follower_x - 1, follower_y)
            return
        # up
        if (leader_y - follower_y == 2) and (leader_x == follower_x):
            self.knots[follower].updatePosition(follower_x, follower_y + 1)
            return
        # down
        if (leader_y - follower_y == -2) and (leader_x == follower_x):
            self.knots[follower].updatePosition(follower_x, follower_y - 1)
            return
        # up right diag
        if (leader_y - follower_y == 2) and (leader_x - follower_x == 1):
            self.knots[follower].updatePosition(follower_x + 1, follower_y + 1)
            return
        if (leader_y - follower_y == 1) and (leader_x - follower_x == 2):
            self.knots[follower].updatePosition(follower_x + 1, follower_y + 1)
            return
        if (leader_y - follower_y == 2) and (leader_x - follower_x == 2):
            self.knots[follower].updatePosition(follower_x + 1, follower_y + 1)
            return
        # up left diag
        if (leader_y - follower_y == 2) and (leader_x - follower_x == -1):
            self.knots[follower].updatePosition(follower_x - 1, follower_y + 1)
            return
        if (leader_y - follower_y == 1) and (leader_x - follower_x == -2):
            self.knots[follower].updatePosition(follower_x - 1, follower_y + 1)
            return
        if (leader_y - follower_y == 2) and (leader_x - follower_x == -2):
            self.knots[follower].updatePosition(follower_x - 1, follower_y + 1)
            return
        # down right
        if (leader_y - follower_y == -2) and (leader_x - follower_x == 1):
            self.knots[follower].updatePosition(follower_x + 1, follower_y - 1)
            return
        if (leader_y - follower_y == -1) and (leader_x - follower_x == 2):
            self.knots[follower].updatePosition(follower_x + 1, follower_y - 1)
            return
        if (leader_y - follower_y == -2) and (leader_x - follower_x == 2):
            self.knots[follower].updatePosition(follower_x + 1, follower_y - 1)
            return
        # down left
        if (leader_y - follower_y == -2) and (leader_x - follower_x == -1):
            self.knots[follower].updatePosition(follower_x - 1, follower_y - 1)
            return
        if (leader_y - follower_y == -1) and (leader_x - follower_x == -2):
            self.knots[follower].updatePosition(follower_x - 1, follower_y - 1)
            return
        if (leader_y - follower_y == -2) and (leader_x - follower_x == -2):
            self.knots[follower].updatePosition(follower_x - 1, follower_y - 1)
            return

    def move_head(self, direction, quantity):
        if direction == 'R':
            for i in range(quantity):
                curr_x, curr_y = self.knots[0].getPosition()
                self.knots[0].updatePosition(curr_x + 1, curr_y)
                for j in range(1, len(self.knots)):
                    self.move_next(j - 1, j)
            return
        if direction == 'L':
            for i in range(quantity):
                curr_x, curr_y = self.knots[0].getPosition()
                self.knots[0].updatePosition(curr_x - 1, curr_y)
                for j in range(1, len(self.knots)):
                    self.move_next(j - 1, j)
            return
        if direction == 'U':
            for i in range(quantity):
                curr_x, curr_y = self.knots[0].getPosition()
                self.knots[0].updatePosition(curr_x, curr_y + 1)
                for j in range(1, len(self.knots)):
                    self.move_next(j - 1, j)
            return
        if direction == 'D':
            for i in range(quantity):
                curr_x, curr_y = self.knots[0].getPosition()
                self.knots[0].updatePosition(curr_x, curr_y - 1)
                for j in range(1, len(self.knots)):
                    self.move_next(j - 1, j)
            return

with open('9_data.txt', 'r') as file:
    instructions = file.read().splitlines()
head = Knot(0, 0)
tail = Knot(0, 0)
knots = [head, tail]
board = Board(knots)
for instruction in instructions:
    dir_quant = instruction.split()
    direction = dir_quant[0]
    quant = int(dir_quant[1])
    board.move_head(direction, quant)

"""
board.move_head('R', 5)
board.move_head('U', 3)
print(board.knots[0].getHistory())
print(board.knots[1].getHistory())
"""
print(len(set(board.knots[1].getHistory())))

with open('9_data.txt', 'r') as file:
    instructions2 = file.read().splitlines()

knots = []
for i in range(10):
    knot = Knot(0,0)
    knots.append(knot)

board = Board(knots)

for instruction in instructions2:
    dir_quant = instruction.split()
    direction = dir_quant[0]
    quant = int(dir_quant[1])
    board.move_head(direction, quant)

print()
"""
for i in range(len(knots)):
    print()
    print(len(board.knots[i].getHistory()))
    print(board.knots[i].getHistory())
"""
print(len(set(board.knots[len(knots)-1].getHistory())))
