start_a = 873
start_b = 583

factor_a = 16807
factor_b = 48271

multiples_a = 4
multiples_b = 8
a_values = []
b_values = []

const = 2147483647

class Generator(object):
    def __init__(self,start,factor):
        self.prev_value = start
        self.factor = factor

    def next_value(self):
        self.prev_value = (self.prev_value * self.factor) % const

def start_part1():
    result = 0
    gen_a = Generator(start_a, factor_a)
    gen_b = Generator(start_b, factor_b)

    for i in range(int(4e7)):
        gen_a.next_value()
        gen_b.next_value()
        if bin(gen_a.prev_value)[-16:] == bin(gen_b.prev_value)[-16:]:
            result += 1

    return result

def start_part2():
    result = 0
    gen_a = Generator(start_a, factor_a)
    gen_b = Generator(start_b, factor_b)

    while len(a_values) < int(5e6):
         gen_a.next_value()
         if gen_a.prev_value % multiples_a == 0:
            a_values.append(bin(gen_a.prev_value)[-16:])
       
    while len(b_values) < int(5e6):
        gen_b.next_value()
        if gen_b.prev_value % multiples_b == 0:
            b_values.append(bin(gen_b.prev_value)[-16:])

    for i in range(int(5e6)):
        if a_values[i] == b_values[i]:
            result += 1

    return result

print("Part 1: ", start_part1(), time()-start)
print("Part 2: ", start_part2(), time()-start)
