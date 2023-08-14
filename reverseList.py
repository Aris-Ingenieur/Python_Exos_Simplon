# L'utilisateur de saisit les éléments de la liste
def saisir_liste():
    elements = []
    while True:
        element = input("Entrez un élément de la liste (ou 'fin' pour terminer) : ")
        if element.lower() == 'fin':
            break
        elements.append(element)
    return elements

# Fonction inverse de liste
def inverser_liste(lst):
    return lst[::-1]

# Saisir une liste et inverser son ordre
def main():
    print("Saisissez les éléments de la liste (terminez par 'fin') :")
    ma_liste = saisir_liste()
    liste_inversee = inverser_liste(ma_liste)
    print("La liste inversée est :", liste_inversee)

# Appeler la fonction principale
main()
