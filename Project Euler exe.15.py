'''
Starting in the top left corner of a 2×2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?

'''


def fac(x):
    j = 1
    for i in range(1, x + 1):
        j = j * i
    return j

y = (fac(40) / fac(20) / fac(20))
z = int(y)
print(z)
print(fac(z))
