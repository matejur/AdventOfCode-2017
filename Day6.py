input_string = "11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11"


banks = []
db = []
counter = 0
number = ""
isRunning = True

for char in input_string:
    if char in ["0","1","2","3","4","5","6","7","8","9"]:
        number += char
    else:
        banks.append(int(number))
        number = ""

banks.append(int(number))

while isRunning:
    index = banks.index(max(banks))
    blocks = banks[index]
    banks[index] = 0

    for x in range(blocks):
        index += 1
        if index >= len(banks):
            index -= len(banks)
        banks[index] += 1

    value = "".join(str(bank) for bank in banks)
    
    counter += 1
    if value not in db:
        db.append(value)
    else:
        print("Part 1: ",counter)
        print("Part 2: ",(counter-1) - db.index(value))
        isRunning = False
