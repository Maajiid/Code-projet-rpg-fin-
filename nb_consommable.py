import random as rd

inventaire = {
    "(1) Potions de soin": 0,
    "(2) Potion de régénération": 0,
    "(3) Potion de défense": 0,
    "(4) Potion de rage": 0,
    "(5) Piment": 0
    }


pourcentages = {
    "(1) Potions de soin": 30,
    "(2) Potion de régénération": 15,
    "(3) Potion de défense": 20,
    "(4) Potion de rage": 20,
    "(5) Piment": 15
    }

for p in range(10):
    choix_potion = rd.choices(list(inventaire.keys()), weights=[pourcentages[p] for p in inventaire])
    inventaire[choix_potion[0]] += 1

nb_potions_soin = inventaire["(1) Potions de soin"]

invPotiondeSoin = {"(1) Potion de soin Faible":0, "(2) Potion de soin Moyen":0, "(3) Potion de soin Elevé":0}

pourcentages_s = {"(1) Potion de soin Faible":50, "(2) Potion de soin Moyen":35, "(3) Potion de soin Elevé":15}

for h in range(nb_potions_soin):
    choix_soin = rd.choices(list(invPotiondeSoin.keys()), weights=[pourcentages_s[h] for h in invPotiondeSoin])
    invPotiondeSoin[choix_soin[0]] += 1

print("Inventaire :")
for potion, quantite in inventaire.items():
    print(f"{potion}: {quantite}")

print("Type de potions de soin :")
for potion, quantite in invPotiondeSoin.items():
    print(f"{potion}: {quantite}")
