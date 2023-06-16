import random

class Personne:
    def __init__(self, nom):
        self.nom = nom
        self.annee = 0
        self.temps = 0

def Saisie():
    t = []
    while True:
        nom = input("Entrez le nom de la personne (ou 'q' pour quitter) : ")
        if nom == 'q':
            break
        personne = Personne(nom)
        t.append(personne)
    return t

def calculAnnee(t, annee_min, annee_max):
    for personne in t:
        periode_valide = False
        while not periode_valide:
            periode = input(f"{personne.nom}, choisissez une période en années pour votre voyage (entre {annee_min} et {annee_max}) : ")
            if periode.isdigit():
                periode = int(periode)
                if abs(periode) >= 10_000:
                    print("La période choisie doit être inférieure à 10 000 ans.")
                else:
                    periode_valide = True
                    annee_depart = random.randint(personne.annee - abs(periode), personne.annee + abs(periode))
                    personne.annee = annee_depart

def calculTemps(t):
    for personne in t:
        temps = abs(personne.annee - 2017) // 10 * 10
        personne.temps = temps

t = Saisie()
calculAnnee(t, -10_000, 10_000)
calculTemps(t)

for personne in t:
    print(f"Nom: {personne.nom}, Année: {personne.annee}, Temps: {personne.temps} secondes")

reponse = input("Prendriez-vous ce risque ? (oui/non) : ")
if reponse.lower() == 'oui':
    print("Bonne chance dans votre voyage temporel !")
else:
    print("Une sage décision !")
