# A róka libát lop a faluból, a hét minden napján egyet. Ezek súlyát tároltuk el a libak.txt-ben. A farkas várja a falu határában a rókát és a 3 kg-nál nehezebb libát elveszi, a kisebbeket meghagyja a rókánál.

# 0. Beolvasás
libak=[]
with open("libak.txt") as fin:
    for suly in fin:
        libak.append(int(suly.strip()))
print(libak)
# 1. Hány kiló libát evett a róka a héten?
roka_kilo=0
for liba in libak:
    if liba <=3:
        roka_kilo+=liba
print(f"{roka_kilo} kiló libát evett a róka.")
# 2. Átlagosan hány kilósak a rókánál maradt libák?
roka_db=0
for liba in libak:
    if liba <= 3:
        roka_db += 1
print(f"Átlagosan {roka_kilo/roka_db} kilósak a rókánál maradt libák.")
# 3. Előfordult-e, hogy a róka legalább 3kg-os libát lopott? 
# Eldöntés
van=False
for liba in libak:
    if liba >=3:
        van=True
        break

if van==True:
    print("Igen")
    
else:
    print("Nem")
# 4. Előfordult-e, hogy a róka kisebb libát lopott, mint az előző napon?
# 5. Hányadik napon sikerült először 3kg-nál nehezebb libát lopni?
# 6. Volt-e 6kg súlyú liba, ha volt akkor melyik napon?
# 7. Hány liba jutott a héten a farkasnak?
# 8. Hány kilós volt a rókánál maradó legnagyobb libának?

