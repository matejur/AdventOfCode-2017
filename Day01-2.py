input_string = ""

razmik = len(input_string)/2
sestevek = 0

for number in range(len(input_string)):

    if input_string[number-int(razmik)] == input_string[number]:
        sestevek += int(input_string[number])

print(sestevek)

    
