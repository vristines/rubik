from rc_alg_functions import *

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

SUNE = sequence([R, U, prime(R), U, R, double(U), prime(R)])

FRURUF = conjugate(F, commutator(R, U))

PLL_H = sequence([double(M), U, double(M), double(U), double(M), U, double(M)])
PLL_UA = sequence([R, prime(U), R, U, R, U, R, prime(U), prime(R), prime(U), double(R)])
PLL_UB = double(PLL_UA) # inverse PLL_Ua
PLL_Z = sequence([prime(M), U, double(M), U, double(M), U, prime(M), double(U), double(M)])