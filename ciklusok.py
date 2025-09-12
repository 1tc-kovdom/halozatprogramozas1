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