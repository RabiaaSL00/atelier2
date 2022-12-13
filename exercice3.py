# 3. Écrire un programme pour itérer une liste donnée et compter l'occurrence de chaque élément et créer un dictionnaire pour montrer le nombre de chaque élément.
'''
Exemple :
[11, 45, 8, 11, 23, 45, 23, 45, 89]
Résultat :
{11: 2, 45: 3, 8: 1, 23: 2, 89: 1}
'''
l=[11,45,8,11,23,45,23,45,89]
dict={}
for val in l :
    if val not in dict.keys():
       dict[val]=1
else:
       dict[val]=dict[val]+1
print(dict)

