size=100
array = [size]
pointer = 0

def initialize():
    i=0
    for i in range(size):
        array[i]= "x"

def check(direction):
    give
    if array[pointer-2] == "L": 
            if direction == "R":
                give = "B"
            elif direction == "L":
                give = "S"
            elif direction == "S":
                give = "R"
    elif array[pointer -2] == "S":
        if direction == "L":
            give = "R"
        elif direction == "S":
            give = "B"
    elif array[pointer -2] == "R":
        if direction == "L":
            give = "B"
    return give

def insert(direction):
    string=temp
    if pointer > 1:
        if array[pointer-1] == "B":
            temp = check(direction)
            array[pointer-1]="x"
            pointer = pointer -2
            array[pointer+1]:temp
        else:
            array[pointer+1]:direction

    else:
        array[pointer+1]:direction

def run (junction_number):
    return (array[junction_number])
