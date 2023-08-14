# Fonction factorielle
def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

# L'utilisateur entre un nombre
nombre = int(input("Entrez un nombre : "))

# Calcul et affichage
resultat = factorielle(nombre)
print(f"La factorielle de {nombre} est {resultat}")
