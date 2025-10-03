# B.1. Számok darabszáma: 5
# B.2. Páros számok darabszáma: 3
# AB.3. Sávdiagram:

lista = [2,4,1,8,3]

#1 SzámDB
osszeg = 0
for i in lista:
    osszeg += 1

print(f"A számok darabszáma: {osszeg}")



#2 PárosDB
def parosszamok(lista):
    parosszam_darab=0
    for paros in lista:
        if paros%2==0:
            parosszam_darab+=1
    return parosszam_darab

print(f"A lista páros elemeinek darabszáma: {parosszamok(lista)}")


#3 Sávdiagram
sorok = 5

for i in range (sorok + 1):
    hely=' '* (sorok - i)
    csillag ='*' * (2 * i - 1)
    print(hely + csillag)