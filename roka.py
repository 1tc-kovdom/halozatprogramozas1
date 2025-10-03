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
voltkisebb=0
for index in range(len(libak)-1):
    if libak[index]>libak[index+1]:
        voltkisebb=True
        break
if voltkisebb:
    print("Előfordult hogy a róka kisebb libát lopott, mint az előző napon")

# 5. Hányadik napon sikerült először 3kg-nál nehezebb libát lopni?
index = 0
while not(libak[index]>3):
    index+=1

print(f"{index+1}. napon sikerült először 3kg-nál nehezebb libát lopni.")
# 6. Volt-e 6kg súlyú liba, ha volt akkor melyik napon?
i = 0
while i < len(libak) and not (libak[i] == 6):
    i += 1 
if i < len(libak):
    print(f"Volt 6kg súlyú liba, a {i+1}. napon")
else:
    print ("Nem volt 6kg súlyú liba.")
# 7. Hány liba jutott a héten a farkasnak?
#Megszámlálás
farkas_db = 0
for liba in libak:
    if liba > 3:
        farkas_db+=1
print(f"{farkas_db} db liba jutott a farkasnak.")
# 8. Hány kilós volt a rókánál maradó legnagyobb libának?
#Maximum kiválasztás 
max_i = 0
for i in range(len(libak)):
    if libak[index] > libak[max_i] and libak[index] < 4:
        max_i= i
print(f"{libak[max_i]} kilós volt a rókánál maradó legnagyobb liba")
# 9. Írasd ki a liba_jo.txt fájlba a libák súlyait 10%-al megemelve.
with open("liba_jo.txt", "w", encoding="utf-8") as fout:
    for liba in libak:
        print(liba*1.1, file=fout)