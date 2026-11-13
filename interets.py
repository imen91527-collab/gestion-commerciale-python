# Programme : Calcul des intérêts

# Saisie des données
capital = float(input("Donner le capital initial (DT) : "))
taux = float(input("Donner le taux d'interet (%) : "))
duree = int(input("Donner la duree (en annees) : "))

# Calcul des intérêts simples
interet_simple = capital * (taux / 100) * duree

# Calcul des intérêts composés
montant_compose = capital * (1 + taux / 100) ** duree
interet_compose = montant_compose - capital

# Affichage des résultats
print("\n--- Resultats des interets ---")
print("Capital initial :", capital, "DT")
print("Taux d'interet :", taux, "%")
print("Duree :", duree, "ans")
print("Interet simple :", interet_simple, "DT")
print("Interet compose :", interet_compose, "DT")
print("Montant final compose :", montant_compose, "DT")