s = input('String = ')
new_str=""
for i in s:
    if i.isupper():
        new_str += i.lower()
    elif i.islower():
        new_str += i.upper()
    else:
        new_str += i
print(f"New_string = {new_str}")