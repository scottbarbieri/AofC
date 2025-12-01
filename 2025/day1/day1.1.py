import math
with open("/workspaces/AofC/2025/day1/input.txt", "r") as file:
    input = file.read().splitlines()
count =0
dial = 50
code = 0
for turns in input:
    count += 1
    direction = turns.rstrip("0123456789")
    if direction == "L":
        for i in range(int(turns.lstrip("LR"))):
            dial = dial -1
            if dial < 0: 
                dial = 99
                #print (dial)
    elif direction == "R":
        for i in range(int(turns.lstrip("LR"))):
            dial += 1
            if dial > 99: 
                dial = 0
    print (count, dial)
    if dial == 0:
        code += 1
print (code)