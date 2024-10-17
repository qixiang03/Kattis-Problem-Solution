
no_of_input, diff = [int(x) for x in input().split()]

notes = []
for _ in range(no_of_input):
    notes.append(int(input()))

notes = sorted(notes)
i =0
count = 1
while i < len(notes):
    max = notes[i] + diff

    for j in range(i+1, len(notes)):
        if notes[j] > max:
            print(notes[i], notes[j])
            i = j
            count += 1
            break
    else:
        break
print(count)