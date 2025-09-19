# Kérjünk be 0 végjelű számokat és írj1uk be az összegüket

# osszeg=0
# while True:
#     beszam=int(input("Kérek egy számot: "))
#     if beszam!=0:
#         osszeg=osszeg+beszam
#     else: 
#         break
# print(f"A bekér számok összege: {osszeg}")
# Enter végjelig kérjünk be számokat

# osszeg=0
# while True:
#     be = input("Kérem a számot, enter megnyomávásal kilépsz. : ")
#     if be == "":
#         break 
#     osszeg += int(be)

# print(f"Az összegük: {osszeg}")

# kérj be egy számot 0 tól az utolsó számig irja ki a páros számokat
hatar = int(input("Kérem a számot: "))
posszeg=0
while posszeg!=hatar+1:
    if posszeg % 2==0:
        print(posszeg)
    posszeg+=1