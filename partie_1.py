class Personne:
    def __init__(self, nom, prenom, numero_rue, nom_rue, telephone, code_postal, ville):
        self.nom = nom
        self.prenom = prenom
        self.numero_rue = numero_rue
        self.nom_rue = nom_rue
        self.telephone = telephone
        self.code_postal = code_postal
        self.ville = ville


def saisie_tab():
    annuaire = []
    while True:
        nom = input("Entrez le nom de la personne (ou appuyez sur Entrée pour terminer) : ")
        if not nom:
            break
        prenom = input("Entrez le prénom de la personne : ")
        numero_rue = input("Entrez le numéro dans la rue : ")
        nom_rue = input("Entrez le nom de la rue : ")
        telephone = input("Entrez le numéro de téléphone : ")
        code_postal = input("Entrez le code postal : ")
        ville = input("Entrez la ville : ")

        personne = Personne(nom, prenom, numero_rue, nom_rue, telephone, code_postal, ville)
        annuaire.append(personne)

    return annuaire


def critere_recherche():
    criteres = ['nom', 'prénom', 'numéro de rue', 'nom de rue', 'numéro de téléphone', 'code postal', 'ville']
    while True:
        print("Critères de recherche disponibles :")
        for i, critere in enumerate(criteres, start=1):
            print(f"{i}. {critere}")
        choix = input("Choisissez le numéro correspondant au critère de recherche : ")
        if choix.isdigit() and 1 <= int(choix) <= len(criteres):
            return criteres[int(choix) - 1]
        else:
            print("Choix invalide. Veuillez réessayer.")


def recherche(annuaire, critere):
    valeur_recherche = input(f"Entrez la valeur de recherche pour le critère '{critere}': ")
    resultat = []
    for personne in annuaire:
        if getattr(personne, critere) == valeur_recherche:
            resultat.append(True)
        else:
            resultat.append(False)
    return resultat


def affiche_tab(annuaire, resultat):
    print("Résultats de la recherche :")
    for personne, trouve in zip(annuaire, resultat):
        if trouve:
            print("Nom :", personne.nom)
            print("Prénom :", personne.prenom)
            print("Numéro dans la rue :", personne.numero_rue)
            print("Nom de la rue :", personne.nom_rue)
            print("Numéro de téléphone :", personne.telephone)
            print("Code postal :", personne.code_postal)
            print("Ville :", personne.ville)
            print()


# Programme principal
annuaire = saisie_tab()

while True:
    print("Que souhaitez-vous faire ?")
    choix = input("1. Effectuer une recherche\n2. Quitter\nChoix : ")

    if choix == "1":
        critere = critere_recherche()
        resultat_recherche = recherche(annuaire, critere)
        affiche_tab(annuaire, resultat_recherche)
    elif choix == "2":
        break
    else:
        print("Choix invalide. Veuillez réessayer.")

print("Programme terminé.")
