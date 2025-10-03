lista = [1, 2, 3, 4]

lista.append(5)        # Hozzáad egy elemet a lista végéhez
lista.extend([6, 7])   # Több elemet ad hozzá a lista végéhez
lista.insert(2, 99)    # Beszúrja a 99-et a 2-es indexre

lista.remove(2)        # Eltávolítja az első előfordulását a 2-es elemnek
lista.pop()            # Eltávolítja és visszaadja az utolsó elemet
lista.pop(1)           # Eltávolítja a megadott indexű elemet
lista.clear()          # Törli az összes elemet a listából

lista = [1, 2, 3, 4, 2]
lista.index(2)         # Visszaadja az első 2-es indexét (0-alapú)
lista.count(2)         # Megszámolja, hányszor szerepel a 2

lista.sort()           # Növekvő sorrendbe rendezi a listát
lista.sort(reverse=True)  # Csökkenő sorrendbe rendezi
lista.reverse()        # Megfordítja a lista elemeinek sorrendjét

lista2 = lista.copy()  # Létrehoz egy másolatot

# Függvény	        Leírás
len(lista)	# Lista hossza
sum(lista)	# Elemeinek összege
max(lista)	# Legnagyobb elem
min(lista)	# Legkisebb elem
sorted(lista)	# Rendezett másolatot ad vissza
list(iterable)	# Lista készítése pl. tuple-ből vagy stringből

# Lista bejárása (iterálás)
for item in lista:
    print(item)

# Indexekkel
for i, item in enumerate(lista):
    print(f"Index {i}: érték {item}")

# Lista generálás (List comprehension)
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]