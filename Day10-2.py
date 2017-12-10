numbers = [x for x in range(256)]
current_position = 0
skip_size = 0
lengths_input = "31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33"
ascii_input = [ord(i) for i in lengths_input] + [17, 31, 73, 47, 23]

for i in range(64):
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

print(hex_string)