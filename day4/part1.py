file1 = open("input.txt", 'r')
lines = file1.readlines()
count = 0

for line in lines:
    elfs = line.split(',')
    one = elfs[0].split('-')
    two = elfs[1].strip('\n').split('-')
    if (int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1])) or (int(two[0]) >= int(one[0]) and int(two[1]) <= int(one[1])):
        count += 1
print(count)