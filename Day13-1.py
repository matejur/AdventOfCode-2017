layers = {}
player_pos = -1
severity = 0

class Layer(object):
    def __init__(self, range):
        self.range = range
        self.scanner_pos = 1
        self.forward = True

    def move_scanner(self):
        if self.scanner_pos == 1:
            self.forward = True
        
        if self.scanner_pos == self.range:
            self.forward = False

        if self.forward:
            self.scanner_pos += 1
        else:
            self.scanner_pos -= 1
  
def move_player():
    global player_pos
    global severity
    player_pos += 1
    if type(layers[player_pos]) == Layer:
        if layers[player_pos].scanner_pos == 1:
            severity += layers[player_pos].range * player_pos

with open("input.txt", "r") as f:
    lines = f.readlines()
    num_layers = int(lines[-1].split(": ")[0])
    
    for x in range(num_layers+1):
        layers[x] = None

    for layer in lines:
        layer = layer.strip("\n").split(": ")
        layers[int(layer[0])] = Layer(int(layer[1]))


for x in range(len(layers)):
    move_player()
    for layer in layers.values():
        if type(layer) == Layer:
            layer.move_scanner()

print(severity)
