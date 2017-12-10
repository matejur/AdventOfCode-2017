numbers = [x for x in range(256)]
current_position = 0
skip_size = 0
lengths_input = [31,2,85,1,80,109,35,63,98,255,0,13,105,254,128,33]

for length in lengths_input:
    if current_position > len(numbers):
        current_position -= len(numbers)

    if current_position+length > len(numbers):
        reverse_numbers = []
        for x in range(length):
            if current_position + x > len(numbers)-1:
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
    
print(numbers[0] * numbers[1])
