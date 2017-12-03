velikost = 15
target_number = 48516

array = [[0 for x in range(velikost)] for y in range(velikost)]

avaiable_directions = ["R", "U", "L", "D"]

def print_array(ar):
    for i in range(len(ar)):
        for j in range(len(ar[i])):
            if ar[i][j] != 0:
                print(str(ar[i][j])+"|" , end=' ')
        print()

def move_right(x,y):
    return(x+1,y)

def move_left(x,y):
    return(x-1,y)

def move_up(x,y):
    return(x,y+1)

def move_down(x,y):
    return(x,y-1)

def calculate_sum(x,y):
    sestevek = 0
    for i in range(-1,2):
        for j in range(-1,2):
            sestevek += array[x+i][y+j]    
    return sestevek

def switch_dir():
    temp = avaiable_directions.pop(0)
    avaiable_directions.append(temp)

def main():
    row_length = 0

    sredina = (int(velikost/2), int(velikost/2))
    array[sredina[0]][sredina[1]] = 1
    spot = sredina
    for x in range(100):
        if x%2 == 0:
            row_length+=1

        for y in range(row_length):

            if avaiable_directions[0]=="R":
                spot = move_right(spot[0],spot[1])
            if avaiable_directions[0]=="U":
                spot = move_up(spot[0],spot[1])
            if avaiable_directions[0]=="D":
                spot = move_down(spot[0],spot[1])
            if avaiable_directions[0]=="L":
                spot = move_left(spot[0],spot[1])

            if calculate_sum(spot[0],spot[1]) > target_number:
                print(calculate_sum(spot[0],spot[1]))
                return
            else:
                array[spot[0]][spot[1]] = calculate_sum(spot[0],spot[1])
            

        switch_dir()

main()
print_array(array)
