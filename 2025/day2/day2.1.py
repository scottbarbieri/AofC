with open("/workspaces/AofC/2025/day2/input.txt", "r") as file:
    input = file.read().split(",")
print (input)
count =0
dial = 0
code = 0
for pairs in input:
    count += 1
    #print( pairs.rsplit("-"))
    for i in range(int(pairs.rsplit("-")[0]),int(pairs.rsplit("-")[1])+1):
        #print (i)
        length = len(str(i))
        if length % 2 ==0:
            mid = length // 2
            #print (str(i)[:length - mid])
            if str(i)[:length - mid] == str(i)[length - mid:]:
                print (i)
                code = code + i

print (code)