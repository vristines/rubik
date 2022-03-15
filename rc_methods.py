from rc_core import *
from rc_algs import *



##### CROSS #####

def CFOP_cross(cube):
    def white_to_bottom(cube):
        if (cube.color(1, 1, 0, 'L') == 'W') or (cube.color(1, 1, 2, 'R') == 'W'):
            cube.process(Y)
            cube.print()
        while not (cube.color(2, 1, 1, 'D') == 'W'):
            cube.process(X)
            cube.print()
        return cube
    white_to_bottom(cube)
    """
    1. move white face to the top
    2. find white edges (B, R, G, O), move to UF, 
        repeat U/Y until UF is correct 
        then F2
    """


"""
def white_to_top(cube):
        if (cube[3][1][1] == 0) or (cube[5][1][1] == 0):
            cube.process(Y)
        while cube[1][1][1] != 0:
            cube.process(X)
        return cube
"""



""" def CFOP_PLL(cube):
    match get_color(0, 2, 1, 'F', cube): # SOLVING AT LEAST 1 EDGE
        case 'B': 
            cube.process(double(Y))
        case 'G': 
            cube.process(PLL_H)
        case _ : cube.process(PLL_UA)
    while not (get_color(0, 0, 1, 'B', cube) == get_color(1, 0, 1, 'B', cube)): # ORIENTING FOR LAST 3 EDGES
        cube.process(Y)
    while not (get_color(0, 2, 1, 'F', cube) == get_color(1, 2, 1, 'F', cube)):
        cube.process(PLL_UA) """
    
