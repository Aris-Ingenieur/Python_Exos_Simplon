# Fonction pour afficher les nombres divisibles par 5
def nomb_divisibles_par_5(ma_liste):
    liste_nombre_div_par5=[]
    for nombre in ma_liste:
        if nombre % 5 == 0:
            liste_nombre_div_par5.append(nombre)
    return liste_nombre_div_par5        
   
#Fonction pour saisir la liste
def saisir_liste():
    liste = []
    while True:
        element = input("Entrez un nombre (ou 'fin' pour terminer) : ")
        if element.lower() == 'fin':
            break
        elt=int(element)
        liste.append(elt)
    return liste


# Appeler la fonction et afficher le résultat
ma_liste = saisir_liste()
print("La liste initiale est: " ,ma_liste)
print("La liste des éléments divibles par 5 est: ",nomb_divisibles_par_5(ma_liste))




