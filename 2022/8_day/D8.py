"""
treeeHeights is a 2d mxn matrix of tree height values.
indeces are like this
[0][0]   [0][1] ...   [0][n-1]
[1][0]   [1][1] ...   [1][n-1]
.         .            .
.         .            .
.         .            .
[m-1][0] [m-1][1] ... [m-1][n-1]

outside trees are all visible, 
    quantity = 2n + 2m - 4

parse the interior of the matrix
1 <= m_index <= m-2
1 <= n_index <= n-2

if all tree heights above, below, to the right, and to the left are shorter
than the tree being observed, the tree is visible from the outside. This can be
done using a function.

read data and clean -> have list of strings (2d list)
use for loop to go through the interior elements
for each interior element(tree) call a function passing the index of the tree
and the 2d list
function will look at all trees to the right, left, above and below comparing
the heights and return a bool true if the tree is visible from either the right
left, up, or down. the default will return false meaning the tree is not visible
"""

def visible(m, n, trees):
    height = int(trees[m][n])
    sum_dirs = 0

    for l in range(n-1, -1, -1):
        if int(trees[m][l]) >= height:
            sum_dirs += 1
            break

    if sum_dirs != 1:
        return True

    for r in range(n + 1, len(trees[m]), 1):
        if int(trees[m][r]) >= height:
            sum_dirs += 1
            break

    if sum_dirs != 2:
        return True

    for u in range(m - 1, -1, -1):
        if int(trees[u][n]) >= height:
            sum_dirs += 1
            break

    if sum_dirs != 3:
        return True

    for d in range(m + 1, len(trees), 1):
        if int(trees[d][n]) >= height:
            sum_dirs += 1
            break

    if sum_dirs == 4:
        return False

    return True

def viewScore(m, n, trees):
    height = int(trees[m][n])
    score = 1

    distance = 0
    for l in range(n-1, -1, -1):
        distance += 1
        if int(trees[m][l]) >= height:
            break
    score *= distance

    distance = 0
    for r in range(n + 1, len(trees[m]), 1):
        distance += 1
        if int(trees[m][r]) >= height:
            break
    score *= distance

    distance = 0
    for u in range(m - 1, -1, -1):
        distance += 1
        if int(trees[u][n]) >= height:
            break
    score *= distance

    distance = 0
    for d in range(m + 1, len(trees), 1):
        distance += 1
        if int(trees[d][n]) >= height:
            break
    score *= distance
    return score


with open('8_data.txt', 'r') as file:
    treeHeights = file.read().splitlines()

visibleTrees = 2 * len(treeHeights) + 2 * len(treeHeights[0]) - 4
for m in range(1, len(treeHeights) - 1):
    for n in range(1, len(treeHeights[m]) - 1):
        if visible(m, n, treeHeights):
            visibleTrees += 1

print(visibleTrees)

max_score = 0
for m in range(1, len(treeHeights) - 1):
    for n in range(1, len(treeHeights[m]) - 1):
        score = viewScore(m, n, treeHeights)
        if  score > max_score:
            max_score = score

print(max_score)

