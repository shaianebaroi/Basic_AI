# TASK01

import math
import random

# FUNCTION CODE
def minimax(position, depth, alpha, beta, maximizingPlayer, values):

    if depth == 0:
        return values[position]

    if maximizingPlayer:
        maxEval = float("-inf")
        for child in range(0, 2):
            eval = minimax(child, depth - 1, alpha, beta, False, values)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval

    else:
        minEval = float("inf")
        for child in range(0, 2):
            eval = minimax(child, depth - 1, alpha, beta, True, values)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval


# MAIN CODE

number = input("Enter your Student ID :")
reversed_digits = int(number[7] + number[6])

min_pts = int(number[4])
max_pts = math.ceil(reversed_digits * 1.5)
total_pts = reversed_digits
shuffles = number[3]

pts = []
for count in range(8):
    score = random.randint(min_pts, max_pts)
    # print(score)
    pts.append(score)

# pts = [66, 74, 14, 73, 19, 26, 32, 40]
print("")
print("Generated 8 random points between the minimum and maximum point limits:", pts)

print("Total points to win:", total_pts)

# ALPHA-BETA PRUNING
alpha = float("-inf")
beta = float("inf")
achieved_pts = minimax(0, 3, alpha, beta, True, pts)

print("Achieved point by applying alpha-beta pruning =", achieved_pts)

if achieved_pts >= total_pts:
    print("The winner is Optimus Prime.")
else:
    print("The winner is Megatron.")

# TASK02

print("")
shuffles = int(number[3])
# print(shuffles)

optimus_wins = 0
shuffled_pts = []
for count in range(shuffles):
    score = random.choice(pts)
    if score >= total_pts:
        optimus_wins += 1
    shuffled_pts.append(score)

print("After the shuffle: ")

print("List of all points values from each shuffles:", shuffled_pts)

max_val = max(shuffled_pts)
print("The maximum value of all shuffles:", max_val)

print("Won", optimus_wins, "times out of", shuffles, "number of shuffles")

