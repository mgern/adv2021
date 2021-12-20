f = open("3input")

#oxygen = 
#go through the first digit of each numbers and find the most common
#keep the most common ones
#repeat for the next digit


#convert file into a 2d array
#make array or length of first line

lines = []

for x in f:
    lines.append(x)


#for each column
for x in range(len(lines[0])):
    zeroes = ones = 0
    for y in lines:
        if y[x] == "0":
            zeroes += 1
        else:
            ones += 1
    if zeroes > ones:
        for i in lines:
            if i[x] == "1":
                lines.remove(x)
    else:
        for i in lines:
            if i[x] == "0":
                lines.remove(i)
    print("\n")
    print(lines)
    print(x)

    

O2 = C02 = 0



lifesupport = O2 * C02

print(lifesupport)