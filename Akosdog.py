nevek = ["Tibi","Évi", "Sanyi", "Karcsi", "Lili" ]
nemek = [1,2,1,1,2]

fiunevek=[]
for i in range(len(nevek)):
    if nemek[i]==1:
        fiunevek.append(nevek[i])

print(fiunevek)
print(f"{len(fiunevek)} fiú van")

print(f"{len(fiunevek)/len(nevek)*100}% a fiúk aránya.")