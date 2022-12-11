crates = open("testcrates.txt", 'r').readlines()
instructions = open("testinput.txt", 'r').readlines()
stackone = []
stacktwo = []
stackthree = []


for crate in crates :
    for i in range(1, 4, 11) :
        if crate[i].isalpha() :
            if i == 1:
                stackone.extend(crate[i])
            elif i == 5:
                stacktwo.extend(crate[i])
            elif i == 9:
                stackthree.extend(crate[i])