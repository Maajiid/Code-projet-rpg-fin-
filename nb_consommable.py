import random as rd

inventaire = {"(1) Potions de soin": 0,"(2) Potion de régénération": 0,"(3) Potion de défense": 0,"(4) Potion de rage": 0,"(5) Piment": 0}


for p in range(10):
    potion_choisie = rd.choice(list(inventaire.keys()))
    inventaire[potion_choisie] += 1

print(inventaire)
nb_potions_soin = inventaire["(1) Potions de soin"]

invPotiondeSoin = {"(1) Potion de soin Faible":0, "(2) Potion de soin Moyen":0, "(3) Potion de soin Elevé":0}

for h in range(nb_potions_soin):
    potion_soin_choisie = rd.choice(list(invPotiondeSoin.keys()))
    invPotiondeSoin[potion_soin_choisie] += 1
print(invPotiondeSoin)    
