crates = open("crates.txt", 'r').readlines()
stackone = []
stacktwo = []
stackthree = []
stackfour = []
stackfive = []
stacksix = []
stackseven = []
stackeight = []
stacknine = []

#putting crates in stacks
for crate in crates :
    i = 0
    while (crate[i] != '\n'):
        if crate[i].isalpha():
            if (i == 1) :
                stackone.append(crate[i])
            elif (i == 5) :
                stacktwo.append(crate[i])
            elif (i == 9) :
                stackthree.append(crate[i])
            elif (i == 13) :
                stackfour.append(crate[i])
            elif (i == 17) :
                stackfive.append(crate[i])
            elif (i == 21) :
                stacksix.append(crate[i])
            elif (i == 25) :
                stackseven.append(crate[i])
            elif (i == 29) :
                stackeight.append(crate[i])
            elif (i == 33) :
                stacknine.append(crate[i])
        i += 1

#moving crates around
instructions = open("input.txt", 'r').readlines()

def findstack(number):
    if number == 1:
        return (stackone)
    if number == 2:
        return (stacktwo)
    if number == 3:
        return (stackthree)
    if number == 4:
        return (stackfour)
    if number == 5:
        return (stackfive)
    if number == 6:
        return (stacksix)
    if number == 7:
        return (stackseven)
    if number == 8:
        return (stackeight)
    if number == 9:
        return (stacknine)

for instruction in instructions:
    res = [int(a) for a in instruction.split() if a.isdigit()]
    amount = int(res[0])
    ori = findstack(int(res[1]))
    goal = findstack(int(res[2]))
    while amount > 0:
        goal.insert(0, ori[amount - 1])
        del ori[amount - 1]
        amount -= 1

print("result:", stackone[0], stacktwo[0], stackthree[0], stackfour[0], stackfive[0], stacksix[0], stackseven[0], stackeight[0], stacknine[0])

# right : BQDNWJPVJ