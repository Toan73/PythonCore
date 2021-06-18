a = int(input("Type in a: "))
b = int(input("Type in b: "))
if a < b:
  for x in range(a, b, 1):
    print(x, end = " ")
else:
  for x in range(a, b, -1):
    print(x, end = " ")