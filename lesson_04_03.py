
import math
a = float(input('Insert a: '))
b = float(input('Insert b: '))
c = float(input('Insert c: '))

if a != 0:
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b+math.sqrt(d)) / (2*a)
        x2 = (-b-math.sqrt(d)) / (2*a)
        print(f"Nghiem x1 = {x1}")
        print(f"Nghiem x2 = {x2}")

    else:
        if d == 0:
            x1 = (-b) / (2*a)
            print(f"Nghiem x1 = x2 = {x1}")
        else:
            print("Phuong trinh vo nghiem")
else:
    if b != 0:
        x1 = -c / b
        print(f"Nghiem cua phuong trinh x = {x1}")
    else:
        if c != 0:
            print("Phuong trinh vo nghiem")
        else:
            print("Phuong trinh co vo so nghiem")