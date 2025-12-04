with open("/workspaces/AofC/2025/day3/input.txt", "r") as file:
    input = file.read().splitlines()
#print (input)
code = 0
for banks in input:
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    eleven = 0
    twelve = 0
    for i in range(0,len(banks)-11):
        if int(banks[i]) > one:
            one = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-10):
        if int(banks[i]) > two:
            two = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-9):
        if int(banks[i]) > three:
            three = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-8):
        if int(banks[i]) > four:
            four = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-7):
        if int(banks[i]) > five:
            five = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-6):
        if int(banks[i]) > six:
            six = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-5):
        if int(banks[i]) > seven:
            seven = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-4):
        if int(banks[i]) > eight:
            eight = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-3):
        if int(banks[i]) > nine:
            nine = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-2):
        if int(banks[i]) > ten:
            ten = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-1):
        if int(banks[i]) > eleven:
            eleven = int(banks[i])
            start = i+1
    for i in range(start,len(banks)-0):
        if int(banks[i]) > twelve:
            twelve = int(banks[i])
            start = i+1
    
    code = code + int(str(one)+str(two)+str(three)+str(four)+str(five)+str(six)+str(seven)+str(eight)+str(nine)+str(ten)+str(eleven)+str(twelve))
print (code)