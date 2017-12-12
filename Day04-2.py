counter = 0
isValid = False

with open("input.txt", "r") as f:
    for line in f:
        isValid = False
        row = line.split(" ")
        
        if "\n" in row[-1]:
                row[-1] = row[-1].replace("\n", "")
        temp = row[:]

        db = []
        for key in row:
            if not sorted(key) in db:
                db.append(sorted(key))
                isValid = True
            else:
                isValid = False
                break
            

        if isValid:
            counter += 1

print(counter)
