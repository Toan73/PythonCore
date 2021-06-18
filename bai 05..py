x = int(input('x = '))
sum = 0
for n in range(1,x):
    sum = sum + n
    print(f"n = {n} ; sum = {sum}")
    if sum > x:
        break
print(f"Gia tri n la: {n-1}")