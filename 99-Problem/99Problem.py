string = "99"

val = int(input())


for i in range(1000):

    if val <= 99:
        print(99)
        break

    temp = int(str(i)+ string)
    if temp - 50 <= val < temp +50:
        print(temp)
        break




