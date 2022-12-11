"CrZsJsPPZsGzwwsLwLmpwMDw""".split('\n')

total = 0
def commonchar(sa, sb, sc):
    for i in sa:
        for j in sb:
            if (i == j):
                for h in sc:
                    if (i == h):
                        return(i)


for x in range(0, len(input), 3):
    print(x)
    print(input[x])
    print(input[x+1])
    cc =commonchar(input[x], input[x+1], input[x+2])
    if cc.islower():
        total += ord(cc) - 97 + 1
    else:
        total += ord(cc) - 65 + 26 + 1
    print (total)
