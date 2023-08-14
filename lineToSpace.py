# Fichier en mode lecture
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()

# À ce stade, le fichier est automatiquement fermé (libéré) en sortant du bloc 'with'

# Remplacer les nouvelles lignes par des espaces
contenu_modifie = contenu.replace("\n", " ")

# Afficher le contenu modifié
print(contenu_modifie)
