file1 = open("input.txt", 'r')
lines = file1.readlines()
count = 0

def overlapping_range(peter, pan, tinker, bell):
    if pan < tinker :
        return False
    if peter > bell :
        return False
    return True

for line in lines:
    mine = False
    elfs = line.split(',')
    tinkerbell = elfs[0].split('-')
    peterpan = elfs[1].strip('\n').split('-')
    if overlapping_range(int(tinkerbell[0]), int(tinkerbell[1]), int(peterpan[0]), int(peterpan[1])) :
        count += 1
    elif overlapping_range(int(peterpan[0]), int(peterpan[1]), int(tinkerbell[0]), int(tinkerbell[1])) :
        count += 2
print(count)
