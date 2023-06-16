import os

def nbMotsAvecVoyelle(nomf):
    count = 0
    with open(nomf, 'r') as fichier:
        for ligne in fichier:
            mot = ligne.strip()
            if mot[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
                count += 1
    return count

# Obtenir le chemin du répertoire de travail actuel
repertoire_travail = os.getcwd()

# Construire le chemin complet des fichiers en utilisant le répertoire de travail
nom_fichier1 = os.path.join(repertoire_travail, 'fichier1.txt')
nom_fichier2 = os.path.join(repertoire_travail, 'fichier2.txt')

# Exemple d'utilisation avec les fichiers "fichier1.txt" et "fichier2.txt"
nombre_mots = nbMotsAvecVoyelle(nom_fichier1)
print(nombre_mots)


def compterChaqueMot(nomf_fichier1, nom_fichier2):
    pass


compterChaqueMot(nom_fichier1, nom_fichier2)
