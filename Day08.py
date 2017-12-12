registers = {}
max_number = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n").split(" ")
        register = line[0]
        operation = line[1]
        number_to_add = int(line[2])
        registry_to_check = line[4]
        condition = line[5]
        number_to_compare = int(line[6])

        if register not in registers.keys():
            registers[register] = 0

        if registry_to_check not in registers.keys():
            registers[registry_to_check] = 0

        if condition == "==" and registers[registry_to_check] == number_to_compare:
            pass
        elif condition == "!=" and registers[registry_to_check] != number_to_compare:
            pass
        elif condition == "<" and registers[registry_to_check] < number_to_compare:
            pass
        elif condition == ">" and registers[registry_to_check] > number_to_compare:
            pass
        elif condition == ">=" and registers[registry_to_check] >= number_to_compare:
            pass
        elif condition == "<=" and registers[registry_to_check] <= number_to_compare:
            pass
        else:
            continue

        if operation == "inc":
            registers[register] += number_to_add
        elif operation == "dec":
            registers[register] -= number_to_add

        if registers[register] > max_number:
            max_number = registers[register]

print("Part 1:", max([x for x in registers.values()]), "Part 2:", max_number)
        
            
