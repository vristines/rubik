from rc_graphics import *
from rc_core import *
from rc_algs import *
from rc_methods import *

if __name__ == '__main__':
    cube = init_cube()
    print_cube(cube)
    
    cube = shuffle(1000,cube)
    cube = CFOP_cross(cube)
