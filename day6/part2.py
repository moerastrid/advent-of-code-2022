input = open("input.txt", 'r').readlines()

def different(mychars):
    temp = []
    temp.append(mychars[0])
    i = 1
    while (i < 14) :
        j = 0
        while(j < len(temp)) :
            if (temp[j] == mychars[i]):
                return False
            j += 1
        temp.append(mychars[i])
        i += 1
    return True

for line in input:
    index = 0
    mychars = []
    count = 1
    for charr in line:
        if count <= 14:
            mychars.append(charr)
        else:
            mychars[int((count - 1) % 14)] = charr
        if (count >= 14 and different(mychars) == True):
            print("result : ", count)
            break 
        count += 1

print("result: ", mychars)
