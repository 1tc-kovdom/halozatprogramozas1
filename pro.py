print("Szia", end="")
print("Tibi")
print("Szia", "Tóth", "Karcsi", "!", sep="")
print("Szia Tóth Karcsi!")
nev = "Tóth Karcsi"
print(f"Szia {nev}!")
print("Szia", "Peti", sep="\n", end="!") #\t
#adattipusok
# int()
# float()
# str()
# bool()
# list()
# set()
print()
print(int("5"))
print(float(5))
print(type(str(5.0)))
print(bool(-1))
print(["hétfő", "kedd", "szerda"])
napok= ["hétfő","kedd", "szerda"]
print(f"Napok: {napok}")
nevek = ["Tibi", "Sanyi", "Tibi"]
print (f"Nevek: {set(nevek)}")
print(tuple([1,2,3]))


# HF: git parancsok:
# git init : adott mappa verziókövetésének indítása
# git add . : hozzáadja a fájlt úgy ahogy a pillanatban kinéz
# git config --global user.name : állít egy nevet amit felismer a repository 
# git config -- user.email : állít egy email címet amit felismer a repository
# git clone : egy repository megszerzése URL-en keresztül 
# git commit -m : Elmenti a stage-elt változtatásokat a repositoryba
#                 Megjegyzést fűz hozzá ami leírja mit változtattunk
# git push : felteszi a repositoryba a helyi commitokat

