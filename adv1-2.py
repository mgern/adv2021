#adventofcode21 - 1

f = open("1input", "r")
prev = 0
count = 0
lines = []

a1 = a2 = a3 = 0
for line in f:
    lines.append(int(line))

# print(len(lines) - 2)
for i in range(len(lines) - 2):
    a1 = lines[i]
    a2 = lines[i+1]
    a3 = lines[i+2]
    if prev != 0:
        #is this higher than previous?
        if (a1 + a2 + a3) > prev:
            count += 1

    prev = a1 + a2 + a3



print(count)