import os
a = 0
i = 0
e = 1
while e<100:
    os.system("cls" if os.name=="nt" else "clear")
    if i == 0:
        print(f"{"\n" *a}{"\t" *a} {"\\"}")
    elif i == 1:
        print(f"{"\n" *a}{"\t" *a} {"|"}")
    elif i ==2:
        print(f"{"\n" *a}{"\t" *a} {"/"}")
    elif i ==3:
        print(f"{"\n" *a}{"\t" *a} {"-"}")
    elif i == 4:
        i = 0
    i += 1
    e += 1
    if e==99:
        e=0
        a += 1

    if a==10:
        break
    