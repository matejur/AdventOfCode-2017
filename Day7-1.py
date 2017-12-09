disks = []
above_disks = ""

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n").split("->")
        if len(line) > 1:
            above_disks += line[1].strip(",")
        disks.append(line[0].split(" ")[0])

    for disk in disks:
        if disk not in above_disks:
            print(disk)

    
