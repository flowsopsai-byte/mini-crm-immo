# Nom du prospect : Thomas
# Budget du prospect : 350000
# chat urgent ? (oui/non) : oui

# Prospect qualifié !#


prospects_qualifies = []
total = 0


while True:
    
    nom = input("Quel est votre nom ?")
    budget = int(input("Quel est votre budget?"))
    urgent = input("Votre achat est-il urgent ?")

    print(f"Nom du prospect : {nom} ")
    print(f"Budget du prospect : {budget}")
    print(f"Achat urgent ? (oui/non) : {urgent}")
    print()

    prospect = {"nom": nom, "budget": budget}

    if budget >= 200000 and urgent == "oui":
        print("Prospect qualifié !")
        prospects_qualifies.append(prospect)
        total += budget
         
    else:
        print("Prospect non qualifié")

    print()
    
    reponse = input("Ajouter un autre prospect ? (oui/non) ")

    if reponse == "non":
        break


if len(prospects_qualifies) > 0:
    
    mean = total / len(prospects_qualifies)
    print(f"Nombre de prospects qualifiés : {len(prospects_qualifies)}")
    print ()
    print("Prospects qualifiés :")
    for prospect in prospects_qualifies:
        print(f"{prospect['nom']} - {prospect['budget']}")

    print()
    print(f"Budget total : {total}$")
    print(f"Moyen budget : {mean}$")

else:
    print()
    print("Désolé, aucun prospect qualifié aujourd'hui :-( )")
