key = "ffayrhll"
used_space = 0
rows = []
groups = 0

def get_bits(string):
    current_position = 0
    skip_size = 0
    numbers = [x for x in range(256)]
    for i in range(64):
        ascii_input = [ord(i) for i in string] + [17, 31, 73, 47, 23]
        for length in ascii_input:
            if current_position > len(numbers):
                current_position -= len(numbers)

            if current_position+length > len(numbers):
                reverse_numbers = []
                for x in range(length):
                    if current_position + x > len(numbers)-1:
                        while current_position + x > len(numbers)-1:
                            current_position -= len(numbers)
                        reverse_numbers.append(numbers[current_position+x -len(numbers)])
                    else:
                        reverse_numbers.append(numbers[current_position+x])

                reverse_numbers = reverse_numbers[::-1]

                for x in range(length):
                    if current_position + x > len(numbers)-1:
                        numbers[current_position + x - len(numbers)] = reverse_numbers.pop(0)
                    else:
                        numbers[current_position + x] = reverse_numbers.pop(0)     
            else:
                reverse_numbers = numbers[current_position : current_position+length]
                reverse_numbers = reverse_numbers[::-1]
                numbers[current_position : current_position+length] = reverse_numbers
            current_position += length + skip_size
            skip_size += 1

    dense_hash = []
    block = 0
    for x in range(16):
        block = numbers[x*16:x*16+16]
        dense_hash.append(block[0]^block[1]^block[2]^block[3]^block[4]^block[5]^block[6]^block[7]^block[8]^block[9]^block[10]^block[11]^block[12]^block[13]^block[14]^block[15])

    hex_string = ""
    for x in dense_hash:
        x = "0x{:02x}".format(x)[2:]
        hex_string += x

    return bin(int(hex_string, 16))[2:].zfill(128)

def clear_neighbours(x,y):
    rows[x][y] = groups
    try:
        if rows[x+1][y] == "1":
            clear_neighbours(x+1,y)
    except:
        pass
    try:
        if rows[x-1][y] == "1" and x != 0:
            clear_neighbours(x-1,y)
    except:
        pass
    try:
        if rows[x][y+1] == "1":
            clear_neighbours(x,y+1)
    except:
        pass
    try:
        if rows[x][y-1] == "1" and y != 0:
            clear_neighbours(x,y-1)
    except:
        pass

for x in range(128):
    bits = get_bits(key+"-"+str(x))
    rows.append([i for i in bits])
    for bit in bits:
        if bit == "1":
            used_space += 1

for x in range(len(rows)):
    for y in range(len(rows)):
        if rows[x][y] == "1":
            clear_neighbours(x,y)
            groups += 1

print("Part 1: ", used_space)
print("Part 2: ", groups)