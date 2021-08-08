#Get all 10,000 pieces based on website's algorithm

TETROMINOS = {
    0: {  # I
        0: [(0, 1), (0, 0), (0, -1), (0, -2)],
        1: [(-1, 0), (0, 0), (1, 0), (2, 0)],
        2: [(0, 1), (0, 0), (0, -1), (0, -2)],
        3: [(-1, 0), (0, 0), (1, 0), (2, 0)],
    },
    1: {  # L
        0: [(0, 0), (0, -1), (0, -2), (1, 0)],
        1: [(0, 0), (0, 1), (1, 0), (2, 0)],
        2: [(-1, 0), (0, 0), (0, 1), (0, 2)],
        3: [(-2, 0), (-1, 0), (0, 0), (0, -1)],
    },
    2: {  # J
        0: [(-1, 0), (0, 0), (0, -1), (0, -2)],
        1: [(0, -1), (0, 0), (1, 0), (2, 0)],
        2: [(1, 0), (0, 0), (0, 1), (0, 2)],
        3: [(-2, 0), (-1, 0), (0, 0), (0, 1)],
    },
    3: {  # T
        0: [(0, 1), (-1, 0), (0, 0), (1, 0)],
        1: [(-1, 0), (0, 0), (0, -1), (0, 1)],
        2: [(0, -1), (-1, 0), (0, 0), (1, 0)],
        3: [(1, 0), (0, 0), (0, -1), (0, 1)],
    },
    4: {  # O
        0: [(0, 0), (0, 1), (1, 1), (1, 0)],
        1: [(0, 0), (0, 1), (1, 1), (1, 0)],
        2: [(0, 0), (0, 1), (1, 1), (1, 0)],
        3: [(0, 0), (0, 1), (1, 1), (1, 0)],
    },
    5: {  # S
        0: [(0, 0), (-1, 0), (0, -1), (1, -1)],
        1: [(-1, 0), (-1, -1), (0, 0), (0, 1)],
        2: [(0, 0), (-1, 0), (0, -1), (1, -1)],
        3: [(-1, 0), (-1, -1), (0, 0), (0, 1)],
    },
    6: {  # Z
        0: [(0, 0), (0, -1), (-1, -1), (1, 0)],
        1: [(-1, 0), (-1, 1), (0, 0), (0, -1)],
        2: [(0, 0), (0, -1), (-1, -1), (1, 0)],
        3: [(-1, 0), (-1, 1), (0, 0), (0, -1)],
    }
}

a = 27073
m = 32749
c = 17713
v = 12358

def get_ran(num):
    return (num*a+c)%m

def get_piece(weightIndex, count):
    stateIndex = count % 4
    shapeIndex = -1
    if (weightIndex >= 0  and weightIndex <= 1):
        shapeIndex = 0;
    elif weightIndex > 1 and weightIndex <= 4:
        shapeIndex = 1;
    elif (weightIndex > 4 and weightIndex <= 7) :
        shapeIndex = 2;
    elif (weightIndex > 7 and weightIndex <= 11) :
        shapeIndex = 3;
    elif (weightIndex > 11 and weightIndex <= 16) :
        shapeIndex = 4;
    elif (weightIndex > 16 and weightIndex <= 22) :
        shapeIndex = 5;
    elif (weightIndex > 22) :
        shapeIndex = 6;
    p = TETROMINOS[shapeIndex][stateIndex]
    return shapeIndex*4+stateIndex

def all_piece(v):
    l = []
    for i in range(10000):
        v = get_ran(v)
        p = get_piece(v%29, i)
        l.append[p]
    return l

l = all_piece(v)
f = open('sequence.txt', 'w')
for i in l:
    f.write(str(i)+'\n')

f.close()



    
