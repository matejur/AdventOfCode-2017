programs = []
counter = 0
groups = 0

class Program(object):

    def __init__(self, index, connections, isConnected):
        self.index = index
        self.connections = connections
        self.isConnected = isConnected


with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n").split("<->")
        connections = [int(x) for x in line[1].split(", ")]
        program = Program(line[0], connections, False)
        programs.append(program)

def update_children(parent):
    for child in parent.connections:
        if not programs[child].isConnected:
            programs[child].isConnected = True
            update_children(programs[child])


update_children(programs[0])
groups += 1

for program in programs:
    if program.isConnected:
        counter += 1

for program in programs:
    if not program.isConnected:
        update_children(program)
        groups += 1

print("Part 1: ",counter, " Part 2: ", groups)
