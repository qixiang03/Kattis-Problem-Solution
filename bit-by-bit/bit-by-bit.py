result = []
while True:
    temp = input()
    if temp == "0":
        break
    if temp.isdigit():
        temp_ls = [-1] * 32
        command = []
        for _ in range(int(temp)):
            command.append(input().split())

        for item in command:
            i = 31 - int(item[1])
            if item[0] == "SET":
                temp_ls[i] = 1
            if item[0] == "CLEAR":
                temp_ls[i] = 0
            if item[0] == "AND":
                j = 31 - int(item[2])
                if temp_ls[i] == 1 and temp_ls[j] == 1:
                    temp_ls[i] = 1
                elif temp_ls[i] == 0 or temp_ls[j] == 0:
                    temp_ls[i] = 0
                else:
                    temp_ls[i] = -1
            if item[0] == "OR":
                j = 31 - int(item[2])
                if temp_ls[i] == 1 or temp_ls[j] == 1:
                    temp_ls[i] = 1
                elif temp_ls[i] == 0 and temp_ls[j] == 0:
                    temp_ls[i] = 0
                else:
                    temp_ls[i] = -1

        result.append(temp_ls)

for item in result:
    item = ["?" if x == -1 else str(x) for x in item]
    print("".join(item))
