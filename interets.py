# Programme : Calcul des interets

# Saisie des donnees
capital = float(input("Donner le capital initial (DT) : "))
taux = float(input("Donner le taux d'interet (%) : "))
duree = int(input("Donner la duree (en annees) : "))

# Calcul des interets simples
interet_simple = capital * (taux / 100) * duree

# Calcul des interets composes
montant_compose = capital * (1 + taux / 100) ** duree
interet_compose = montant_compose - capital

# Affichage des resultats
print("Interet simple :", interet_simple, "DT")
print("Interet compose :", interet_compose, "DT")
print("Montant final compose :", montant_compose, "DT")