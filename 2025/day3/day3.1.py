with open("/workspaces/AofC/2025/day3/input.txt", "r") as file:
    input = file.read().splitlines()
#print (input)
count =0
dial = 0
code = 0
for banks in input:
    left = 0
    right = 0
    #print( pairs.rsplit("-"))
    for i in range(0,len(banks)-1):
        #print (int(banks[i]))
        if int(banks[i]) > left:
            left = int(banks[i])
    start = banks.find(str(left))+1
    for i in range(start,len(banks)):
        if int(banks[i]) > right:
            right = int(banks[i])
    code = code + int(str(left)+str(right))
    print (left, right)
        

        #for j in range(1,length+1):
            #x = str(i).count(str(i)[0:j])
            #print (str(i)[0:j])
            #print (x)
            #if x != 1:
                #if x * len(str(i)[0:j]) == length:
                    #print(i)
                    #print (len(str(i)[0:j]))
                    #code=code+i
                    #break


print (code)