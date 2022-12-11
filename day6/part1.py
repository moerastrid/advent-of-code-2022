input = open("input.txt", 'r').readlines()
count = 1

def different(a, b, c, d):
    if (a != b and a != c and a != d):
        if (b != c and b != d):
            if (c != d):
                return True
    return False

for line in input:
    for charr in line:
        if count % 4 == 0:
            one = charr
        if count % 4 == 1:
            two = charr
        if count % 4 == 2:
            three = charr
        if count % 4 == 3:
            four = charr
        if count >= 4 and different(ord(one), ord(two), ord(three), ord(four)) == True:
            print("result : ", count)
            break 
        count += 1
    print(one, two, three, four)


# too low : 1756 