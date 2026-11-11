prospects = [
    {"nom": "Lucas", "budget": 500000, "urgent": False},
    {"nom": "Emma", "budget": 180000, "urgent": True},
    {"nom": "Julie", "budget": 150000, "urgent": False}
]


prospects_qualifie = [] 
total = 0 

for prospect in prospects: 
    if prospect["budget"] >= 200000 and prospect["urgent"] == True:
        prospects_qualifie.append(prospect)
        total += prospect["budget"]


if len(prospects_qualifie) > 0:
    mean = total / len(prospects_qualifie)
    print(f"Nombre de prospects : {len(prospects_qualifie)}")
    print(f"Budget total : {total} $")
    print(f"Budget moyen : {mean} $")

else:
    print("Pas de prospect qualifié ajourd'hui")





