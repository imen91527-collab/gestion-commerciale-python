# Programme : Calcul de la TVA

# Saisie du prix hors taxes
prix_ht = float(input("Donner le prix HT (DT) : "))

# Calcul de la TVA
tva = prix_ht * 0.19

# Calcul du prix toutes taxes comprises
prix_ttc = prix_ht + tva

# Affichage des résultats
print("Montant de la TVA :", tva, "DT")
print("Prix TTC :", prix_ttc, "DT")