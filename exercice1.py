# Créer une liste en choisissant des éléments d'index impair dans la première liste et des éléments d'index pair dans la seconde
''' 
Étant donné deux listes, l1 et l2, écrivez un programme pour créer une troisième liste l3 en choisissant un élément d'indice impair dans la liste l1 et des éléments d'indice pair dans la liste l2.

Exemple : [3, 6, 9, 12, 15, 18, 21] [4, 8, 12, 16, 20, 24,28]

Résultat : [6, 12, 18, 4, 12, 20, 28]
'''
l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
l3=[]
for i in range(0,len(l1)):
    if i%2==1:
        l3.append(l1[i])
for i in range(0,len(l2)):
    if i%2==0:
      l3.append(l2[i])
print(l3)

