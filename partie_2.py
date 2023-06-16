# Fonction récursive divinRec(a, b) pour la division entière a div b
def divinRec(a, b):
    if a < b:
        return 0
    else:
        return 1 + divinRec(a - b, b)

# Fonction récursive puissance(a, b) pour calculer a^b
def puissance(a, b):
    if b == 0:
        return 1
    else:
        return a * puissance(a, b - 1)
print(divinRec(10, 3))  # Résultat: 3
print(puissance(2, 4))  # Résultat: 16
def divinRec(a, b):
    if a < b:
        return 0
    else:
        return 1 + divinRec(a - b, b)
