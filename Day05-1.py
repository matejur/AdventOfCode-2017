index = 0
counter = 0

with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = list(map(int, lines))

    while True:
        next_move = lines[index]
        lines[index] += 1
        index += next_move
        counter += 1
        
        if index > len(lines)-1:
            print(counter)
            break
