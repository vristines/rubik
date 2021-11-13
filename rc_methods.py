from rc_core import *
from rc_algs import *



def CFOP_cross(cube):
    def white_to_top(cube):
        if (cube[3][1][1] == 0) or (cube[5][1][1] == 0):
            cube.process(Y)
        while cube[1][1][1] != 0:
            cube.process(X)
        return cube

    """
    1. move white face to the top
    2. find white edges (B, R, G, O), move to UF, 
        repeat U/Y until UF is correct 
        then F2

    """

    # vespod = U2
    # navrchu = přeskočení dalších kroků
    # nahoře = con((FR),U') + U2
    # vlevo = con(L', U)
    # vpravo = con(R, U)
    # dole = con((F'R),U') + U2

    # WHITE TO TOP 
    white_to_top(cube)

    edges = [((1,0,1),(4,0,1)), ((1,1,0),(5,0,1)),
            ((1,1,2),(3,0,1)), ((1,2,1),(2,0,1)),
            ((0,0,1),(2,2,1)), ((0,1,0),(5,2,1)),
            ((0,1,2),(3,2,1)), ((0,2,1),(4,2,1)),
            ((2,1,0),(5,1,1)), ((3,1,0),(2,1,1)),
            ((4,1,0),(3,1,1)), ((5,1,0),(4,1,1))]
    # BLUE SIDE
    while not cube[2][1][1] == 2:
        cube = process(Y,cube)


    # RED SIDE

    # GREEN SIDE

    # ORANGE SIDE

    

    

    

    """ while cube[0][0][1] * cube[0][1][0] * cube[0][1][2] * cube[0][2][1] == 0:
        if cube[1][2][1] == 0: 
            cube = process(Y, cube) """


    return cube


def CFOP_D_corners(cube):
    def clean_corner(cube):
        while 0 in [cube[2][2][0], cube[0][0][0], cube[5][2][2]]:
            cube = process(sequence([Y, U]), cube)
        return cube

    for i in range(4):
        if 0 in [cube[2][0][0], cube[1][2][0], cube[5][0][2]]:
            if cube[2][0][0] == 0:
                clean_corner(cube)
                cube = process(commutator(prime(U), prime(L)),cube)
            if cube[1][2][0] == 0:
                clean_corner(cube)
                cube = process(commutator(prime(L), prime(U)),cube)
            if cube[5][0][2] == 0:
                clean_corner(cube)
                cube = process(commutator(U, F),cube)
        cube = process(U, cube)

    for i in range(4):
        while cube[0][0][2] != 0:
            cube = process(SEXY,cube)
        cube = process(Y, cube)


    return cube



def CFOP_PLL_2L(cube):
    # find headlights
        # if 4 HL = done
        # if 1 HL = alg
        # if 0 HL = alg, find and again alg

    

    for i in range(4):
        if cube[2][0][1] == cube[2][1][1]:
            cube = process(double(X), cube)
            break
        cube = process(X, cube)
    
    while not (cube[2][0][1] == cube[2][1][1]):
        cube = process(PLL_U, cube)
            