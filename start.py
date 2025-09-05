# feladat: négyzet/téglalap kerületének számítása 
def beker(alakzat, oldal):
    oldalhossz = int(input(f"Kérem a {alakzat} {oldal} oldalának hosszát [cm]: "))
    """Bekéri az 'alakzat' 'oldal' oldalának hosszát"""
    return oldalhossz

def teglalapKerulete(a, b):
    """Kiszámolja az 'a' és 'b' oldal ismeretében a téglalap kerületét. K= 2*(a+b)"""
    kerulet = 2 * (a + b)
    return kerulet

def kiir(alakzat, kerulet):
    """Kiírja az 'alakzat' 'kerulet' - ét"""
    print(f"A {alakzat} kerülete {kerulet}cm.")
# input
mit = input("[T]églalap vagy [N]égyzet kerületét számoljam [T|N]? ")
if mit.upper() == "N":
    alap = int(input("Kérem a négyzet alapját [cm]: "))
    # calculation
    kerulet = teglalapKerulete(alap, alap)
    # output 
    print(f"A négyzet kerülete: {kerulet} cm.")
elif mit.upper() == "T":
    a_oldal = beker("téglalap", "a")
    b_oldal = beker("téglalap", "b")
    # calculation
    kerulet = teglalapKerulete(a_oldal, b_oldal)
    # output 
    print(f"A téglalap kerülete: {kerulet} cm.")
else: 
    print("Hibás választás. Kilépek!")