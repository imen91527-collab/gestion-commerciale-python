# Programme : Calcul du total des ventes

quantite = int(input("Donner la quantite vendue : "))
prix_unitaire = float(input("Donner le prix unitaire (DT) : "))

if quantite < 0 or prix_unitaire < 0:
    print("Erreur : les valeurs doivent etre positives.")
else:
    total_ventes = quantite * prix_unitaire
    print("Le total des ventes est :", total_ventes, "DT")