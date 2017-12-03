import time

input_number = 265149
def move_right(x,y,razmik):
    return(x+razmik,y)

def move_left(x,y,razmik):
    return(x-razmik,y)

def move_up(x,y,razmik):
    return(x,y+razmik)

def move_down(x,y,razmik):
    return(x,y-razmik)

def xrazmik(x,y, razmik):
    return(x+razmik,y)

def yrazmik(x,y, razmik):
    return(x,y+razmik)

start_time = time.time()
row_length = 0
steps = 0
razmik = 0
counter = 0

x = 1

coord = (0,0)
               
while x<input_number:
    if steps%2 == 0:
        row_length += 1
    if x+row_length > input_number:
            while x < input_number:
                razmik+=1
                x+=1
            break

    x += row_length
    steps += 1

step_razmik = 1    
for step in range(steps):
    if step%4 == 0:
        coord = move_right(coord[0],coord[1],step_razmik)
        #print("right", coord)
    if step%4 == 1:
        coord = move_up(coord[0],coord[1],step_razmik)
        #print("up", coord)
    if step%4 == 2:
        coord = move_left(coord[0],coord[1],step_razmik)
        #print("left", coord)
    if step%4 == 3:
        coord = move_down(coord[0],coord[1],step_razmik)
        #print("down", coord)
    if step%2 != 0 and step != 0:
        step_razmik += 1

if range(steps+1)[-1]%4 == 0:
    coord = xrazmik(coord[0],coord[1], razmik)
if range(steps+1)[-1]%4 == 1:
    coord = yrazmik(coord[0],coord[1], razmik)
if range(steps+1)[-1]%4 == 2:
    coord = xrazmik(coord[0],coord[1], -razmik)
if range(steps+1)[-1]%4 == 3:
    coord = yrazmik(coord[0],coord[1], -razmik)
    

print(abs(coord[0])+abs(coord[1]), time.time()-start_time)
#print("Korak: {}, Razmik: {}, Coord: {}". format(steps, razmik, coord))    
