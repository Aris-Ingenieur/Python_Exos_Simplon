# Demander à l'utilisateur de saisir sa propre liste
def saisir_liste():
    elements = []
    while True:
        element = input("Entrez un élément de la liste (ou 'fin' pour terminer) : ")
        if element.lower() == 'fin':
            break
        elements.append(element)
    return elements

# Afficher la liste
def afficher_liste(liste):
    print("La liste saisie est :", liste)

# Demander à l'utilisateur ce qu'il veut modifier
def modifier_liste(liste):
    element_a_modifier = input("Entrez l'élément que vous souhaitez modifier : ")
    nouvelle_valeur = input("Entrez la nouvelle valeur : ")
    if element_a_modifier in liste:
        index = liste.index(element_a_modifier)
        liste[index] = nouvelle_valeur
        print("La liste modifiée est :", liste)
    else:
        print("L'élément à modifier n'a pas été trouvé dans la liste.")

# Saisir une liste, afficher la liste, puis demander à l'utilisateur de modifier un élément
def main():
    print("Saisissez les éléments de la liste (terminez par 'fin') :")
    ma_liste = saisir_liste()
    afficher_liste(ma_liste)
    modifier_liste(ma_liste)

# Appeler la fonction principale
main()
