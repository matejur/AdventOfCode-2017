garbage = False
ignore_next = False
total_score = 0
score = 1
garbage_score = 0

with open("input.txt", "r") as f:
    for line in f:
        for char in line:
            if ignore_next:
                ignore_next = False
                continue

            elif char == "!":
                ignore_next = True
                continue

            elif char == "{" and not garbage:
                total_score += score
                score += 1

            elif char == "}" and not garbage:
                score -= 1

            elif char == "<" and not garbage:
                garbage = True

            elif char == ">" and garbage:
                garbage = False

            elif garbage:
                garbage_score += 1
            


print ("Part 1: ", total_score, "Part 2: ", garbage_score)