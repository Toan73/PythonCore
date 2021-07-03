s = input('String = ')
s_new = ''
ky_tu_dau = s[0]
for i in s:
    if i == ky_tu_dau:
        ky_tu ='$'
    else:
        ky_tu = i
    s_new = s_new + ky_tu

print(f"New String = {s_new}")