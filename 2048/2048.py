
temp = [input().split() for _ in range(4)]
deck = [int(block) for item in temp for block in item]
move = int(input())

def add(i1, i2, i3, i4):
    valid = [x for x in [i1, i2, i3, i4] if x != 0]
    result = []
    i = 0

    while i < len(valid):

        if i < len(valid) - 1 and valid[i] == valid[i+1]:
            result.append(valid[i]*2)
            i+=2
        else:
            result.append(valid[i])
            i+=1

    return result + [0] * (4 - len(result))

def row(l1,l2,l3,l4):
    for item in [l1,l2,l3,l4]:
        for block in item:
            print(block, end=' ')
        print()

def column(l1,l2,l3,l4):
    temp = [l1,l2,l3,l4]
    for i in range(4):
        for j in range(4):
            print(temp[j][i], end=" ")
        print()

match move:
    case 0: #left
        first = add(deck[0], deck[1], deck[2], deck[3])
        second = add(deck[4], deck[5], deck[6], deck[7])
        third = add(deck[8], deck[9], deck[10], deck[11])
        fourth = add(deck[12], deck[13], deck[14], deck[15])
        row(first, second, third, fourth)


    case 1: #up
        first = add(deck[0], deck[4], deck[8], deck[12])
        second = add(deck[1], deck[5], deck[9], deck[13])
        third = add(deck[2], deck[6], deck[10], deck[14])
        fourth = add(deck[3], deck[7], deck[11], deck[15])
        column(first, second, third, fourth)

    case 2: #right
        first = add(deck[3], deck[2], deck[1], deck[0])[::-1]
        second = add(deck[7], deck[6], deck[5], deck[4])[::-1]
        third = add(deck[11], deck[10], deck[9], deck[8])[::-1]
        fourth = add(deck[15], deck[14], deck[13], deck[12])[::-1]
        row(first, second, third, fourth)


    case 3: #down
        first = add(deck[12], deck[8], deck[4], deck[0])[::-1]
        second = add(deck[13], deck[9], deck[5], deck[1])[::-1]
        third = add(deck[14], deck[10], deck[6], deck[2])[::-1]
        fourth = add(deck[15], deck[11], deck[7], deck[3])[::-1]
        column(first, second, third, fourth)


