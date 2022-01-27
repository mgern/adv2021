f = open("3input")

# gamma = 0 #gamma = bits of most common bits in each row
# epsilon = 0 #least common = gamma xor'ed with 11111
counts = [0,0,0,0,0,0,0,0,0,0,0,0]
linecount = 0
for x in f:
    # binary = int(x, 2)
    # print(binary)
    counts[0] += int(x[0])
    counts[1] += int(x[1])
    counts[2] += int(x[2])
    counts[3] += int(x[3])
    counts[4] += int(x[4])
    counts[5] += int(x[5])
    counts[6] += int(x[6])
    counts[7] += int(x[7])
    counts[8] += int(x[8])
    counts[9] += int(x[9])
    counts[10] += int(x[10])
    counts[11] += int(x[11])
    # counts[12] += int(x[12])
    
    linecount += 1

print(counts)

gamma = []
for n in counts:
    if n > linecount / 2:
        gamma.append("1")
    else:
        gamma.append("0")

gamma = ''.join(gamma)
epsilon = gamma.replace("1","4").replace("0","1").replace("4","0")

power = int(gamma,2) * int(epsilon, 2)
print(power)
