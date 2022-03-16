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
