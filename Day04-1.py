counter = 0
isValid = False

with open("input.txt", "r") as f:
    for line in f:
        isValid = False
        row = line.strip("\n").split(" ")
        temp = list(row)
        
        for key in row:
            temp.remove(key)
            if key in temp:
                isValid = False
                break
            else:
                isValid = True
            temp.append(key)
            

        if isValid:
            counter += 1

print(counter)
