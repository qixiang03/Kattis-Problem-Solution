no_of_rock = int(input())
rocks = [int(x) for x in input().split()]
indexed_rocks = [(weight, index) for index, weight in enumerate(rocks)]

indexed_rocks.sort()

result = [0]*no_of_rock

for rank, (weight, ori_index) in enumerate(indexed_rocks):
    result[ori_index] = rank


print(" ".join(map(str, result)))
