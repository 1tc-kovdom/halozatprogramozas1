# ciklusok

lista = [1, 2, 3, 4, 5, 6, 23, 53, 66, 92, 244]

def osszegez(lista):
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg

def parosszamok(lista):
    parosszam_darab=0
    for paros in lista:
        if paros%2==0:
            parosszam_darab+=1
    return parosszam_darab

print(f"A lista elemeinek összege: {osszegez(lista)}")

print(f"A lista páros elemeinek darabszáma: {parosszamok(lista)}")

# Irass ki egy sorba 5 *-ot

print("*"*5)

for i in range(5):
    print("*", end="")
print()

# rajzolj piramist:

sor=5  
for i in range(sor+1):
    hely=' '*(sor-i)
    csillag='*'*(2*i-1)
    print(hely+csillag)

# csinálj szorzótáblát 10*10

for i in range (1, 11):
    for j in range (1,  11):
        print(f"{i*j:3}", end=" ")

    print()


    