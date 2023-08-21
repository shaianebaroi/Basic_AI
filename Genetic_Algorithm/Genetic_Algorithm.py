import random
import numpy as np


def fitness_function(population, runs):
    fitness = []
    for count in range(len(population)):
        set = population[count]

        total = 0
        for count2 in range(len(set)):
            total += int(set[count2]) * runs[count2]

        fitness.append(total)
    return fitness
    # HIGHER THE FITNESS VALUE, BETTER THE CHOICE


def random_selection(population, fitness_values):

    # print("Population:", population)
    # print("Fitness Values: ", fitness_values)
    a = np.asarray(fitness_values)

    size = 1
    replace = True

    # ASSIGNING PROBABILITES ACCORDING TO WEIGHTS
    for count in range(len(a)):
        probability = 1 / np.abs(a - target_score)
    # print(probability)

    sum = 0
    for count in range(len(probability)):
        sum += probability[count]
    # print(sum)

    p = []
    for count in range(len(probability)):
        p.append(probability[count] / sum)
    # print("Probability: ", p)

    parent = np.random.choice(a, size, replace, p)

    for count in range(len(fitness_values)):
        if parent == fitness_values[count]:
            # print(population[count])
            return population[count]


def crossover(x, y):
    num = random.randint(0, len(x))
    # print("Crossover Index:", num)
    child = x[0:num:1] + y[num : len(y) : 1]
    return child


def mutate(child):
    num = int(random.randint(0, len(child) - 1))
    num2 = str(random.randint(0, 1))
    child = child[0:num:1] + num2 + child[num + 1 : len(child) : 1]
    return child


def genetic_algorithm(population, fitness_values, mutation_threshold):

    new_population = []
    new_fitness_values = []
    n = 10000

    while n > 0:
        x = random_selection(population, fitness_values)
        y = random_selection(population, fitness_values)
        # print("Parent1:", x)
        # print("Parent2:", y)

        child = crossover(x, y)
        # print("Child :", child)

        var = random.uniform(0, 1)
        # print("Var :", var)
        # print("Mutation Threshold: ", mutation_threshold)
        if var < float(mutation_threshold):
            child = mutate(child)
            # print("Mutated Child:", child)

        if child not in new_population:
            new_population.append(child)

        population = new_population
        # print("Population: ", population)

        new_fitness_values = fitness_function(population, runs)
        if new_fitness_values[-1] == target_score:
            print(child)
            # print("Found")
            return child
        fitness_values = new_fitness_values
        n -= 1
    print("-1")


# MAIN CODE
file = open("input3.txt", "r")

line = file.readline().rstrip()
array = line.split()

batsmen = int(array[0])
target_score = int(array[1])

# print("Number of batsmen:", batsmen)
# print("Target Score:", target_score)

players = []
runs = []
for count in range(batsmen):
    line = file.readline().rstrip()
    array = line.split()
    players.append(array[0])
    runs.append(int(array[1]))
print(players)
# print("Runs by Players:", runs)

# GENERATING POPULATION
population = []
for count in range(4):
    string = ""
    for count2 in range(batsmen):
        string += str(random.randint(0, 1))
    population.append(string)
# population = ["11100101", "01111011", "10011110", "00001101"]
# print("Population:", population)

# CALCULATING FITNESS VALUES
fitness_values = fitness_function(population, runs)
# print("Fitness Values:", fitness_values)

genetic_algorithm(population, fitness_values, mutation_threshold=0.3)

file.close()
