
# Programme : Calcul de la marge commerciale

# Saisie des données
prix_achat = float(input("Donner le prix d'achat (DT) : "))
prix_vente = float(input("Donner le prix de vente (DT) : "))

# Calcul de la marge
marge = prix_vente - prix_achat

# Affichage des informations
print("\n--- Résultat de la vente ---")
print("Prix d'achat :", prix_achat, "DT")
print("Prix de vente :", prix_vente, "DT")
print("Marge commerciale :", marge, "DT")

# Conclusion
if marge > 0:
    print("Conclusion : vente rentable.")
elif marge == 0:
    print("Conclusion : vente sans bénéfice ni perte.")
else:
    print("Conclusion : vente à perte.")