# Programme : Calcul du total des ventes

# Saisie des données
quantite = int(input("Donner la quantite vendue : "))
prix_unitaire = float(input("Donner le prix unitaire (DT) : "))

# Calcul du total des ventes
total_ventes = quantite * prix_unitaire

# Affichage des résultats
print("\n--- Resultat des ventes ---")
print("Quantite vendue :", quantite)
print("Prix unitaire :", prix_unitaire, "DT")
print("Total des ventes :", total_ventes, "DT")