# Programme : Calcul de la TVA

# Saisie du prix hors taxes
prix_ht = float(input("Donner le prix HT (DT) : "))

# Calcul de la TVA
taux_tva = 0.19
montant_tva = prix_ht * taux_tva

# Calcul du prix TTC
prix_ttc = prix_ht + montant_tva

# Affichage des résultats
print("\n--- Résultat du calcul de TVA ---")
print("Prix HT :", prix_ht, "DT")
print("Taux de TVA :", taux_tva * 100, "%")
print("Montant de TVA :", montant_tva, "DT")
print("Prix TTC :", prix_ttc, "DT")