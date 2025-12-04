with open("/workspaces/AofC/2025/day2/input.txt", "r") as file:
    input = file.read().split(",")
print (input)
code = 0
for pairs in input:
    #print( pairs.rsplit("-"))
    for i in range(int(pairs.rsplit("-")[0]),int(pairs.rsplit("-")[1])+1):
        length = len(str(i))
        for j in range(1,length+1):
            x = str(i).count(str(i)[0:j])
            #print (str(i)[0:j])
            #print (x)
            if x != 1:
                if x * len(str(i)[0:j]) == length:
                    print(i)
                    print (len(str(i)[0:j]))
                    code=code+i
                    break


print (code)
