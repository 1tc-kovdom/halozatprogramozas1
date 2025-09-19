lista = [ 2,4,1,8,3 ]
# A1 : Lista elemeinek összege 
osszeg = 0
for szam in lista: 
    osszeg+=szam

print(f"A1: A Lista elemeinek összege: {osszeg} ")
print(f"A1: A Lista elemeinek összege: {sum(lista)} ")

# B1 : Lista elemeinek darabszáma
darab = 0
for szam in lista:
    darab += 1

print(f"Lista elemeinek darabszáma: {darab}")
print(f"Lista elemeinek darabszáma: {len(lista)}")

# A2 : Páros számok átlaga
paros_osszeg = 0
paros_db = 0
for szam in lista:
    if szam %2==0:
        paros_osszeg+=szam
        paros_db+=1
    
print(f"A páros számok átlaga: {paros_osszeg / paros_db:.3f}")

# B2 : A páros számok darabszába 
print(f"A páros számok darabszáma: {paros_db}")

# A2, B2 : Páros számok kiválogatása
parosok_lista = [szam for szam in lista if szam %2 == 0]
# parosok_lista = [2, 4, 8]
print(f"A páros számok átlaga: {sum(parosok_lista)/len(parosok_lista):.2f}")
print(f"A páros számok darabszáma: {len(parosok_lista)}")

# AB3 : Jelenítsd meg sávdiagramon a listát
for szam in lista:
    print(szam, "*" * szam)
