

with open('2_data.txt', 'r') as file:
    data_list = file.readlines()

data_list = [element.strip() for element in data_list]

"""
    A ROCK
    B PAPER
    C SCISSORS

    X ROCK
    Y PAPER
    Z SCISSORS

    SCORE
    YOUR SELECTION
        X - ROCK - 1
        Y - PAPER - 2
        Z - SCISSORS - 3
    RESULT
        LOST - 0
        DRAW - 3
        WIN  - 6

    NINE SCORE POSSIBILITIES
    A ROCK - X ROCK -> DRAW (1 + 3 = 4)
    A ROCK - Y PAPER -> WIN (2 + 6 = 8)
    A ROCK - Z SCISSORS -> LOSE (3 + 0 = 3)
    B PAPER - X ROCK -> LOSE (1 + 0 = 1)
    B PAPER - Y PAPER -> DRAW (2 + 3 = 5)
    B PAPER - Z SCISSORS -> WIN (3 + 6 = 9)
    C SCISSORS - X ROCK -> WIN (1 + 6 = 7)
    C SCISSORS - Y PAPER -> LOSE (2 + 0 = 2)
    C SCISSORS - Z SCISSORS -> DRAW (3 + 3 = 6)
"""
scores = {'A X': 4, 'A Y': 8, 'A Z': 3, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 7, 'C Y': 2, 'C Z': 6}

total_score = 0
for element in data_list:
    total_score += scores[element]

print(data_list)
print(total_score)

"""
    NEW DECRYPTIONS

    A ROCK
    B PAPER
    C SCISSORS

    X LOSE
    Y DRAW
    Z WIN

    SCORE
    YOUR SELECTION
        ROCK - 1
        PAPER - 2
        SCISSORS - 3
    RESULT
        X - LOSE - 0
        Y - DRAW - 3
        Z - WIN  - 6

    NINE SCORE POSSIBILITIES
    A ROCK - X LOSE -> SCISSORS (3 + 0 = 3)
    A ROCK - Y DRAW -> ROCK (1 + 3 = 4)
    A ROCK - Z WIN -> PAPER (2 + 6 = 8)
    B PAPER - X LOSE -> ROCK (1 + 0 = 1)
    B PAPER - Y DRAW -> PAPER (2 + 3 = 5)
    B PAPER - Z WIN -> SCISSORS (3 + 6 = 9)
    C SCISSORS - X LOSE -> PAPER (2 + 0 = 2)
    C SCISSORS - Y DRAW -> SCISSORS (3 + 3 = 6)
    C SCISSORS - Z WIN -> ROCK (1 + 6 = 7)
"""

new_scores = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7}

total_new_score = 0
for element in data_list:
    total_new_score += new_scores[element]

print(total_new_score)
