def double(A1):
    return A1 + A1

def prime(A1):
    return A1 + A1 + A1

def sequence(A1):
    new = []
    for i in A1:
        new += i
    return new

def conjugate(A1, A2):
    return A1 + A2 + prime(A1)

def commutator(A1, A2):
    return A1 + A2 + prime(A1) + prime(A2)

## CORE MOVEMENTS
CORE_U = 'U'
CORE_X = 'X'
CORE_Y = 'Y'

## CUBE MOVEMENTS
X = [CORE_X]
Y = [CORE_Y]
Z = conjugate(X, Y)

## SIDE MOVEMENTS
U = [CORE_U]
D = conjugate(double(X), U)
F = conjugate(X, U)
B = conjugate(prime(X), U)
L = conjugate(prime(Y), F)
R = conjugate(Y, F)

## WIDE SIDE MOVEMENTS
UW = sequence([double(X), U, double(X), Y])
DW = conjugate(double(X), UW)
FW = conjugate(X, UW)
BW = conjugate(prime(X), UW)
LW = conjugate(prime(Y), FW)
RW = conjugate(Y, FW)

## MIDDLE MOVEMENTS
E = sequence([prime(UW),U])
M = conjugate(prime(Z), E)
S = conjugate(prime(X), E)

SEXY = commutator(R, U)














