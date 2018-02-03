
size = 1000
array = [size]
pt = 0

#def initialize():
 #   i=0
  #  for i in range(0,size):
   #     array[i]= "x"

def check(direction):
    if array[pt-2] == "L": 
        if direction == "R":
            give = "B"
        elif direction == "L":
            give = "S"
        elif direction == "S":
            give = "R"
    elif array[pt -2] == "S":
        if direction == "L":
            give = "R"
        elif direction == "S":
            give = "B"
    elif array[pt -2] == "R":
        if direction == "L":
            give = "B"
    return give

def insert(direction):
    global pt
    if pt > 1 :
        if array[pt-1] == "B":
            temp = check(direction)
            array[pt-1]="x"
            pt = pt -2
            array[pt+1]:temp
        else:
            array[pt+1]:direction
    else:
        array[pt+1]:direction

def run (junction_number):
    return (array[junction_number])

w, h = 12, 12
#Matrix = [[0 for x in range(w)] for y in range(h)] 
Matrix= [                                                   #here 5 is obstacle; 0 is path; 9 is the destination;
        [0,0,0,0,0,0,0,0,0,0,0,0,9],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,5,5,5,5,0,0,0],
        [0,0,0,0,0,0,5,5,5,5,0,0,0],
        [0,0,0,5,0,0,5,5,5,5,0,0,0],
        [0,0,5,5,0,0,5,5,5,5,0,0,0],
        [5,5,5,5,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,5],
        [0,0,0,0,0,0,0,0,5,5,5,5,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,5,5,5,5,5,0,0,0,0,0],
        [0,0,5,5,5,5,5,5,5,0,0,0,0]]
       #above 12,0 is the source.

junction = 0
i = 12
j = 0
#initialize()
while Matrix[i-1][j] != 9 or Matrix[i][j+1] != 9:
    print("Inside While")
    if i>0 and Matrix[i-1][j] == 0:
        insert("L")
        i = i-1
    elif i == 0 and Matrix[i][j+1] == 0:
        insert("S")
        j = j+1
    elif j < 12 and Matrix[i][j+1] == 0:
        insert("S")
        j = j+1
    elif j == 12 and Matrix[i-1][j] == 0:
        insert("L")
        i = i-1
    elif Matrix[i+1][j] == 0:
        insert("R")
        i = i+1
    else :
        insert("B")
        j = j-1
    junction = junction + 1
else :
    if Matrix[i-1][j] == 9:
        insert("L")
        junction =junction + 1
    elif Matrix[i][j+1] == 9:
        insert("S")
        junction = junction + 1

print(junction)