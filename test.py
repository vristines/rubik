""" for i in [(x,y,z,a) for x in range(3) for y in range(3) \
        for z in range(3) for a in range(6)]:
    print(i) """

for i in range(5):
    for j in range(5):
        if i == j == 3:
            print(i,j,3)
x = 'F'
ffff = f'{x}'
print (ffff)
print(type(ffff))