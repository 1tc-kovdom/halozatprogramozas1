lista = [ 1,4,5,2,8,12,74,6 ]

osszeg = 0

for szam in lista:
    osszeg+=szam

print (f"A számok összege: {osszeg}")

db = 0

for szam in lista:
    db +=1

print (f"A számok darab száma: {db}.")

paros=[]
for szam in lista:
    if szam %2==0:
        paros.append(szam)
print(f"A páros számok: {paros}")

paratlandb=0
for szam in lista:
    if szam %2!=0:
        paratlandb+=1
print(f"A páratlan számok: {paratlandb}")

# keresztnevek bekérése, új névig

nevek = []
while True:
    benev=input("Kérem a nevet: ")
    if benev in nevek:
        break
    nevek.append(benev)
print(nevek)
        