with open("input.txt", "r") as f:
    
    sestevek = 0
    
    for row in f:
        row_numbers = []
        number = ""
        
        for char in row:
            if char in ["0","1","2","3","4","5","6","7","8","9"]:
                number += char
            else:
                row_numbers.append(int(number))
                number = ""

        for number1 in row_numbers:
            for number2 in row_numbers:
                if number1%number2 == 0 and number1 != number2:
                    sestevek += number1/number2

print(sestevek)
