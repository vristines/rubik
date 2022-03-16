class Cubelet:
    def __init__(self, a, b, c):
        cols = 6 * [' ']
        if a == 2: cols[0] = 'W'
        if a == 0: cols[1] = 'Y'
        if b == 2: cols[2] = 'B'
        if c == 2: cols[3] = 'R'
        if b == 0: cols[4] = 'G'
        if c == 0: cols[5] = 'O'
        self.D, self.U, self.F, self.R, self.B, self.L = cols
    
    def rotX(self):
        self.B, self.D, self.F, self.U = self.U, self.B, self.D, self.F
        
    def rotY(self):
        self.F, self.R, self.B, self.L = self.R, self.B, self.L, self.F