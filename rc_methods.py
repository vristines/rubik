from rc_core import *
from rc_algs import *

def white_to_bottom(cube):
    if (cube[3][1][1] == 0) or (cube[5][1][1] == 0):
        cube = process(Y,cube)
    while cube[0][1][1] != 0:
        cube = process(X,cube)
    return cube

def CFOP_cross(cube):
    """
    1. move white face to the bottom
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
    white_to_bottom(cube)


    return cube


