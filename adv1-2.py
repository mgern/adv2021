#adventofcode21 - 1

f = open("1input", "r")
prev = 0
count = 0
for line in f:
    if prev != 0:
        if int(line) > prev:
            count += 1
    prev = int(line)

print(count)