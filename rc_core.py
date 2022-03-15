from termcolor import colored
from random import randint

class Cubelet:
    def __init__(self,cols):
        self.D = f'{cols[0]}'
        self.U = f'{cols[1]}'
        self.F = f'{cols[2]}'
        self.R = f'{cols[3]}'
        self.B = f'{cols[4]}'
        self.L = f'{cols[5]}'
    
    def rotX(self):
        self.B, self.D, self.F, self.U = self.U, self.B, self.D, self.F
        
    def rotY(self):
        self.F, self.R, self.B, self.L = self.R, self.B, self.L, self.F


class Cube:
    def __init__(self):
        ## CUBE GENERATION
        data = []
        for a in range(3):
            mid_1 = []
            for b in range(3):
                mid_2 = []
                for c in range(3):
                    """
                    pozdeji aplikovat:
                    if a == 2: add W
                    if a == 0: add Y
                    if b == 2: add B
                    if c == 2: add R
                    if b == 0: add G
                    if c == 0: add O
                    """
                    mid_2.append('')
                mid_1.append(mid_2)
            data.append(mid_1)

        ## CUBE COLORIZATION

        data[0][0][0] = Cubelet(' Y  GO')
        data[0][0][1] = Cubelet(' Y  G ')
        data[0][0][2] = Cubelet(' Y RG ')
        data[0][1][0] = Cubelet(' Y   O')
        data[0][1][1] = Cubelet(' Y    ')
        data[0][1][2] = Cubelet(' Y R  ')
        data[0][2][0] = Cubelet(' YB  O')
        data[0][2][1] = Cubelet(' YB   ')
        data[0][2][2] = Cubelet(' YBR  ')
        data[1][0][0] = Cubelet('    GO')
        data[1][0][1] = Cubelet('    G ')
        data[1][0][2] = Cubelet('   RG ')
        data[1][1][0] = Cubelet('     O')
        data[1][1][1] = Cubelet('      ')
        data[1][1][2] = Cubelet('   R  ')
        data[1][2][0] = Cubelet('  B  O')
        data[1][2][1] = Cubelet('  B   ')
        data[1][2][2] = Cubelet('  BR  ')
        data[2][0][0] = Cubelet('W   GO')
        data[2][0][1] = Cubelet('W   G ')
        data[2][0][2] = Cubelet('W  RG ')
        data[2][1][0] = Cubelet('W    O')
        data[2][1][1] = Cubelet('W     ')
        data[2][1][2] = Cubelet('W  R  ')
        data[2][2][0] = Cubelet('W B  O')
        data[2][2][1] = Cubelet('W B   ')
        data[2][2][2] = Cubelet('W BR  ')
        self.data = data
    
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

    def process(self, alg):  
        for m in alg:
            match m:
                case 'U': self.phys_U()
                case 'X': self.phys_X()
                case 'Y': self.phys_Y()
        #self.print()

    def shuffle(self, num):
        poss = ['U', 'X', 'Y']
        shuf = []
        for i in range(num):
            shuf.append(poss[randint(0,2)])
        self.process(shuf)

    def color(a, b, c, f, cube):
        match f: 
            case 'U': return cube.data[a][b][c].U
            case 'D': return cube.data[a][b][c].D
            case 'F': return cube.data[a][b][c].F
            case 'B': return cube.data[a][b][c].B
            case 'L': return cube.data[a][b][c].L
            case 'R': return cube.data[a][b][c].R
            case __ : return ' '