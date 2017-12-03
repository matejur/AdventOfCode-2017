input_string = ""

prev_number = None
sestevek = 0

for number in input_string:

    if prev_number == number:
        sestevek += int(number)
    else:
        prev_number = number;

if input_string[0] == input_string[-1]:
    sestevek += int(input_string[0])

print(sestevek)

    
