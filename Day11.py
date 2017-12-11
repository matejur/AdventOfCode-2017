x = 0
y = 0
z = 0

max_distance = 0

with open("input.txt", "r") as f:
    for line in f:
        directions = line.split(",")
    for direction in directions:
        if direction == "n":
            y+=1
            z-=1
        if direction == "s":
            y-=1
            z+=1
        if direction == "ne":
            z-=1
            x+=1
        if direction == "nw":
            y+=1
            x-=1
        if direction == "sw":
            z+=1
            x-=1
        if direction == "se":
            y-=1
            x+=1

        if max_distance < (abs(x) + abs(y) + abs(z))/2:
            max_distance = (abs(x) + abs(y) + abs(z))/2
            
print("Part 1: ",(abs(x) + abs(y) + abs(z))/2 - 1, " Part 2: ", max_distance)
