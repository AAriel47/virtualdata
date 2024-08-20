import os
import random
import math
ab = random.randint(0,10)
a = 0
i = 0
e = 1
while e<50:
    #ab = random.randint(0,10)
    os.system("cls" if os.name=="nt" else "clear")
    if i == 0:
        print(f"{"\n" *ab}{"\t" *ab} {"\\"}")
    elif i == 1:
        print(f"{"\n" *ab}{"\t" *ab} {"|"}")
    elif i ==2:
        print(f"{"\n" *ab}{"\t" *ab} {"/"}")
    elif i ==3:
        print(f"{"\n" *ab}{"\t" *ab} {"-"}")
    elif i == 4:
        i = -1
    i += 1
    e += 1
    if e==49:
        ab = random.randint(0,10)
        e=0
        a += 1

    if a==8:
        a=0
        e=0
        i = 0
        print("SSS")
        while e<50:
            #ab = random.randint(0,10)
            os.system("cls" if os.name=="nt" else "clear")
            if i == 0:
                print(f"{"\t" *ab} {"\\"}")
            elif i == 1:
                print(f"{"\t" *ab} {"|"}")
            elif i ==2:
                print(f"{"\t" *ab} {"/"}")
            elif i ==3:
                print(f"{"\t" *ab} {"-"}")
            elif i == 4:
                i = -1
            i += 1
            e += 1
            if e==49:
                ab = random.randint(0,3)
                e=0
                a += 1
            if a==12:
                
                #a=0
                #e=0
                #i = 0
                break
        break
    