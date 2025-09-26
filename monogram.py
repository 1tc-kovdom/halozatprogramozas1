# név bekérése, adja vissza a monogramját a névnek
nev=input("Kérem a nevet: ")
szavak=nev.split()
monogram=""
for szo in szavak:
    if szo:  
        monogram+=szo[0].upper()
        
print("A monogramod:", monogram)