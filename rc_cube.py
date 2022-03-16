from termcolor import colored
from rc_cubelet import *
from random import choice

class Cube:
    def __init__(self):
        self.data = [[[Cubelet(a, b, c) for c in range(3)] for b in range(3)] for a in range(3)]
        for i in range(1000):
            self.process(choice(['U', 'X', 'Y']))
    
    def process(self, alg):  
        for m in alg:
            match m:
                case 'U': self.phys_U()
                case 'X': self.phys_X()
                case 'Y': self.phys_Y()
        #self.print()

    def print(self):
        COLORS = ['white', 'yellow', 'blue', 'red', 'green', 'magenta', 'grey']
        def black():
            print('  ',end='')
        def cl(a,b,c,d):
            colS = ''
            match d:
                case 0: colS = self.data[a][b][c].D
                case 1: colS = self.data[a][b][c].U
                case 2: colS = self.data[a][b][c].F
                case 3: colS = self.data[a][b][c].R
                case 4: colS = self.data[a][b][c].B
                case 5: colS = self.data[a][b][c].L
            match colS:
                case 'W' : colI = 0
                case 'Y' : colI = 1
                case 'B' : colI = 2
                case 'R' : colI = 3
                case 'G' : colI = 4
                case 'O' : colI = 5
                case _   : colI = 6
            print(colored('██', COLORS[colI]),end='')
        def eol():
            print()
        data = self.data
        ########### # ########### # ########### # ########### # ########### # ########### # ########### # ########### # ########### # ########### # ########### # ########### #
        eol()
        black()     ; black()     ; black()     ; cl(0,0,0,1) ; cl(0,0,1,1) ; cl(0,0,2,1) ; print()
        black()     ; black()     ; black()     ; cl(0,1,0,1) ; cl(0,1,1,1) ; cl(0,1,2,1) ; print()
        black()     ; black()     ; black()     ; cl(0,2,0,1) ; cl(0,2,1,1) ; cl(0,2,2,1) ; print()
        cl(0,0,0,5) ; cl(0,1,0,5) ; cl(0,2,0,5) ; cl(0,2,0,2) ; cl(0,2,1,2) ; cl(0,2,2,2) ; cl(0,2,2,3) ; cl(0,1,2,3) ; cl(0,0,2,3) ; cl(0,0,2,4) ; cl(0,0,1,4) ; cl(0,0,0,4) ; print()
        cl(1,0,0,5) ; cl(1,1,0,5) ; cl(1,2,0,5) ; cl(1,2,0,2) ; cl(1,2,1,2) ; cl(1,2,2,2) ; cl(1,2,2,3) ; cl(1,1,2,3) ; cl(1,0,2,3) ; cl(1,0,2,4) ; cl(1,0,1,4) ; cl(1,0,0,4) ; print()
        cl(2,0,0,5) ; cl(2,1,0,5) ; cl(2,2,0,5) ; cl(2,2,0,2) ; cl(2,2,1,2) ; cl(2,2,2,2) ; cl(2,2,2,3) ; cl(2,1,2,3) ; cl(2,0,2,3) ; cl(2,0,2,4) ; cl(2,0,1,4) ; cl(2,0,0,4) ; print()
        black()     ; black()     ; black()     ; cl(2,2,0,0) ; cl(2,2,1,0) ; cl(2,2,2,0) ; print()
        black()     ; black()     ; black()     ; cl(2,1,0,0) ; cl(2,1,1,0) ; cl(2,1,2,0) ; print()
        black()     ; black()     ; black()     ; cl(2,0,0,0) ; cl(2,0,1,0) ; cl(2,0,2,0) ; print()
        eol()

    def phys_U(self): 
        data = self.data
        for a in range(3):
            for b in range(3):
                data[0][a][b].rotY()
        data[0][0][0], data[0][2][0], data[0][2][2], data[0][0][2] = data[0][2][0], data[0][2][2], data[0][0][2], data[0][0][0]
        data[0][0][1], data[0][1][0], data[0][2][1], data[0][1][2] = data[0][1][0], data[0][2][1], data[0][1][2], data[0][0][1]

    def phys_X(self):
        data = self.data
        for c in range(3):
            for a in range(3):
                for b in range(3):
                    data[a][b][c].rotX()
            data[0][0][c], data[0][2][c], data[2][2][c], data[2][0][c] = data[0][2][c], data[2][2][c], data[2][0][c], data[0][0][c]
            data[0][1][c], data[1][2][c], data[2][1][c], data[1][0][c] = data[1][2][c], data[2][1][c], data[1][0][c], data[0][1][c]

    def phys_Y(self):
        data = self.data
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    data[a][b][c].rotY()
            data[a][0][0], data[a][2][0], data[a][2][2], data[a][0][2] = data[a][2][0], data[a][2][2], data[a][0][2], data[a][0][0]
            data[a][0][1], data[a][1][0], data[a][2][1], data[a][1][2] = data[a][1][0], data[a][2][1], data[a][1][2], data[a][0][1]


    """ def phys_F(self):
        rot_list = [(a,2,c) for a in range(3) for c in range(3)]
        for coord in rot_list:
            for c in range(3):
                self.data[coord[0]][coord[1]][coord[2]].rotZ()
        self.data[0][2][0], self.data[0][2][2], self.data[2][2][2], self.data[2][2][0] = self.data[2][2][0], self.data[0][2][0], self.data[0][2][2], self.data[2][2][2] 
        self.data[0][2][1], self.data[1][2][2], self.data[2][2][1], self.data[1][2][0] = self.data[1][2][0], self.data[0][2][1], self.data[1][2][2], self.data[2][2][1]
    """


        # NEW KERNEL MOVES : .. F ..  Fw .. Y 

        # upravit podle schématu:
        # vytvořit seznam původních a nových souřadnic 
        # projet paralelně listy a udělat self.data[x[l1[0]]][x[l1[1]]][x[l1[2]]] = self.data[y[l2[0]]][y[l2[1]]][y[l2[2]]]