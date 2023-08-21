# MAIN CODE
file = open("new.txt", "r")

matrix = []
for line in file:
    array = list(file.readline().split(" "))

print(array)

