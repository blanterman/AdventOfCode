# Day 4 part 1
# Playing Bingo against an octopus

# clean up the next bingo board data
def get_next_board(list):
    board = []
    line = []
    for element in list:
        line = element.split()
        board.append(line)
    return board

# Check for horizontal and vertical bingo
def check_for_bingo(board):
    # Check for horizontal bingo
    for line in board:
        total = line.count("*")
        if total == 5:
            return True
    # Check for vertical bingo
    elements = len(board[0])
    for vertical_pos in range(elements):
        total = 0
        for line in board:
            if line[vertical_pos] == "*":
                total = total + 1
        if total == 5:
            return True
    return False

# Add all the left over numbers on the board together
def sumup(board):
    total=0
    for line in board:
        for word in line:
            if word != "*":
                total = total + int(word)
    return total

# Read data into a list and clean up the data
with open("4_1.txt", "r") as data:
    data_list = data.read().split("\n")
instructions_str = data_list[0].split(",")

# Create lists for all the data needed to compute the score for the winning
# or losing board.
totals_to_bingo = []
sum_of_remaining = []
last_choices = []

# Go through each board
for index in range(2, len(data_list), 6):
    # Get the next board
    board = get_next_board(data_list[index :index + 5])
    # keep track of the number of numbers drawn as bingo is played
    choices = 0
    # Go through all the bingo numbers in order and mark them on the board
    for selection in instructions_str:
        choices = choices + 1
        # Mark the board with a *
        for line in board:
            try:
                line[line.index(selection)] = "*"
            except ValueError:
                pass
        # Check for bingo after the board is marked
        if check_for_bingo(board):
            # if there is bingo, add the number of bingo numbers, the sum of
            # the remaining numbers, and the last bingo number called to their
            # lists used to find the best/worst board and compute a score.
            totals_to_bingo.append(choices)
            sum_of_remaining.append(sumup(board))
            last_choices.append(int(selection))
            break
# Compute the best and worst board from the data and print the results
index_of_min = totals_to_bingo.index(min(totals_to_bingo))
index_of_max = totals_to_bingo.index(max(totals_to_bingo))
print("The first to win will have a score of {}.".format(sum_of_remaining[index_of_min] * last_choices[index_of_min]))
print("The last to win will have a score of {}.".format(sum_of_remaining[index_of_max] * last_choices[index_of_max]))

