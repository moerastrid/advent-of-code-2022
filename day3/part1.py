".... lgnNhsqVqNqNpPlvZvDDDGlZZ""".split('\n')

def commonchar(sa, sb):
    for i in sa:
        for j in sb:
            if i == j:
                return(i)

total = 0
for line in input:
    slice_one = slice(0, int(len(line) / 2))
    slice_two = slice(int(len(line) / 2), int(len(line)))
    cc = commonchar(line[slice_one], line[slice_two])
    if cc.islower():
        total += ord(cc) - 97 + 1
    else:
        total += ord(cc) - 65 + 26 + 1
print("total : {}".format(total))