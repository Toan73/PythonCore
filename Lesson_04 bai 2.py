import math
x_str = input('x = ')
y_str = input('y = ')
z_str = input('z = ')
x = float(x_str)
y = float(y_str)
z = float(z_str)
f = (x+y+z)/(x**2+y**2+1) - abs (x-z*math.cos(y))
f_str = str(f)
print('Gia tri cua F = ' + f_str)