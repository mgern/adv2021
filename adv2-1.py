f = open("2input")

hoz = 0
dep = 0

for x in f:
    dir = x.split()[0]
    value = int(x.split()[1])
    # print(dir)
    if(dir == "up"):
        dep -= value
    if(dir == "down"):
        dep += value
    if(dir == "forward"):
        hoz += value
    # if(dir == "up"):
    #     dep -= value
print(hoz * dep)
