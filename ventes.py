# Programme : Calcul du total des ventes

# Saisie des donnees
quantite = int(input("Donner la quantite vendue : "))
prix_unitaire = float(input("Donner le prix unitaire (DT) : "))

# Calcul du chiffre d'affaires
total_ventes = quantite * prix_unitaire

# Affichage du resultat
print("Le total des ventes est :", total_ventes, "DT")