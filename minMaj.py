# Fonction
def alterner_majuscules_minuscules(mot):
    resultat = ""
    for i, indice in enumerate(mot):
        if i % 2 == 0:
            resultat += indice.upper()  # en maj si l'indice est pair
        else:
            resultat += indice.lower()  # en minus si l'indice est impair
    return resultat

# Demander à l'utilisateur un mot
mot = input("Entrez un mot : ")

# Appeler la fonction et afficher le résultat
resultat = alterner_majuscules_minuscules(mot)
print(resultat)
