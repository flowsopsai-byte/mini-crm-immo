
prospects = [
    {"nom": "Thomas", "budget": 350000},
    {"nom": "Marc", "budget": 150000},
    {"nom": "Sophie", "budget": 280000},
    {"nom": "Paul", "budget": 420000}
]

name = input("Quel prospect recherchez-vous ?")
trouve = False 

for prospect in prospects:
    if prospect["nom"] == name:
        trouve = True 
        print()
        print(f"{prospect['nom']} - {prospect['budget']}")
        print()
        
        while True:

            ope = input("Vous souhaitez Augmenter ou diminuer votre budget? Repondez + ou - : ")

            if ope == "+" or ope == "-":
                break
            
            else:
                print("Entrée non valide")

        nouveau = float(input("De quel pourcentage souhaiter vous modifier votre budget?"))
        zob = nouveau / 100
        
        if ope == "+":
            prospect['budget'] = prospect['budget'] + (prospect['budget'] * zob)
        
        if ope == "-":
            prospect['budget'] = prospect['budget'] - (prospect['budget'] * zob)               
    
        print()
        print(f"Nouveau budget : {prospect['budget']}")
        print("Budget mis à jour !")
        print()

if trouve == False:
    print("Aucun prospect trouvé")

print(prospects)


