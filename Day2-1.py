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

        sestevek += max(row_numbers) - min(row_numbers)


print(sestevek)
