from termcolor import colored

COLORS = ['white', 'yellow', 'blue', 'red', 'green', 'magenta']

"""
Use "rich" or "termcolor" to color the sides

Default colors
D   down side       white       0
U   up side         yellow      1
F   front side      blue        2
R   right side      red         3
B   back side       green       4  
L   left side       orange      5  // now magenta

"""

def init_cube():
    cube = [[3*[i] for j in range(3)] for i in range(6)]
    return cube

def print_cube(cube):
    def black():
        print('  ',end='')
    def cl(f,r,c):
        color = COLORS[cube[f][r][c]]
        print(colored('██', COLORS[cube[f][r][c]]),end='')
    def eol():
        print()
    ######### # ######### # ######### # ######### # ######### # ######### # ######### # ######### # ######### # ######### # ######### # ######### #
    eol()
    black()   ; black()   ; black()   ; cl(1,0,0) ; cl(1,0,1) ; cl(1,0,2) ; eol()
    black()   ; black()   ; black()   ; cl(1,1,0) ; cl(1,1,1) ; cl(1,1,2) ; eol()
    black()   ; black()   ; black()   ; cl(1,2,0) ; cl(1,2,1) ; cl(1,2,2) ; eol()
    cl(5,0,0) ; cl(5,0,1) ; cl(5,0,2) ; cl(2,0,0) ; cl(2,0,1) ; cl(2,0,2) ; cl(3,0,0) ; cl(3,0,1) ; cl(3,0,2) ; cl(4,0,0) ; cl(4,0,1) ; cl(4,0,2) ; eol()
    cl(5,1,0) ; cl(5,1,1) ; cl(5,1,2) ; cl(2,1,0) ; cl(2,1,1) ; cl(2,1,2) ; cl(3,1,0) ; cl(3,1,1) ; cl(3,1,2) ; cl(4,1,0) ; cl(4,1,1) ; cl(4,1,2) ; eol()
    cl(5,2,0) ; cl(5,2,1) ; cl(5,2,2) ; cl(2,2,0) ; cl(2,2,1) ; cl(2,2,2) ; cl(3,2,0) ; cl(3,2,1) ; cl(3,2,2) ; cl(4,2,0) ; cl(4,2,1) ; cl(4,2,2) ; eol()
    black()   ; black()   ; black()   ; cl(0,0,0) ; cl(0,0,1) ; cl(0,0,2) ; eol()
    black()   ; black()   ; black()   ; cl(0,1,0) ; cl(0,1,1) ; cl(0,1,2) ; eol()
    black()   ; black()   ; black()   ; cl(0,2,0) ; cl(0,2,1) ; cl(0,2,2) ; eol()
    eol()

