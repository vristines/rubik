from rc_graphics import *
from random import randint

def double(move,obj):
    return move(move(obj))

def inverse(move,obj):
    return move(move(move(obj)))

def face(face):
    new = [3*[-1] for j in range(3)]
    new[0][0] = face[2][0]
    new[0][1] = face[1][0]
    new[0][2] = face[0][0]

    new[1][0] = face[2][1]
    new[1][1] = face[1][1]
    new[1][2] = face[0][1]

    new[2][0] = face[2][2]
    new[2][1] = face[1][2]
    new[2][2] = face[0][2]
    
    return new

def phys_X(cube):
    return [double(face, cube[4]),
            cube[2],
            cube[0],
            face(cube[3]),
            double(face, cube[1]),
            inverse(face, cube[5])]

def phys_Y(cube):
    return [inverse(face, cube[0]),
            face(cube[1]),
            cube[3], 
            cube[4], 
            cube[5], 
            cube[2]]

def phys_U(cube):
    cube[1] = face(cube[1])
    cube[2][0], cube[3][0], cube[4][0], cube[5][0] = cube[3][0], cube[4][0], cube[5][0], cube[2][0]
    return cube

def process(alg,cube):  
    for m in alg:
        match m:
            case 'U': cube = phys_U(cube)
            case 'X': cube = phys_X(cube)
            case 'Y': cube = phys_Y(cube)
    print_cube(cube)
    return cube

def shuffle(num,cube):
    poss = ['U', 'X', 'Y']
    shuf = []
    for i in range(num):
        shuf.append(poss[randint(0,2)])
    return process(shuf, cube)

