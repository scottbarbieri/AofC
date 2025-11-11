with open("/workspaces/AofC/2024/day1/input.txt", "r") as file:
    input = file.read().splitlines()
total = 0
game_number = 0
for games in input:
    pulls = games.split(": ")[1].split("; ")
    game_number += 1
    #print (pulls)
    red_max = 0
    blue_max = 0
    green_max = 0
    for s in pulls:
        for cube in s.split(", "):
            #print (cube)
            number, color = cube.split(" ")
            number = int(number)
            if color == "red":
                if number > red_max:
                    red_max = number
            if color == "green":
                if number > green_max:
                    green_max = number       
            if color == "blue":
                if number > blue_max:
                    blue_max = number                
    print (red_max, green_max, blue_max)
    if red_max < 13 and green_max < 14 and blue_max < 15:
        total = total + game_number
print (total)