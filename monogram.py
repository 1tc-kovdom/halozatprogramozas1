# név bekérése, adja vissza a monogramját a névnek
kettobetus = ["sz", "ty", "gy", "ny", "cs", "dz", "ly", "zs"]
harombetus = ["dzs"]

nev = input("Kérem a nevet: ")
nevek = nev.split()
monogram = ""

for szo in nevek:
    if szo[:3] in harombetus:
        monogram+=szo[:3].capitalize()
    elif szo[:2] in kettobetus:
        monogram+=szo[:2].capitalize()
    else:
        monogram+=szo[0].upper()

print("A monogramod:", monogram)