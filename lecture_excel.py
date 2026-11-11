import openpyxl

classeur = openpyxl.load_workbook("prospects_immo copy.xlsx")

print(classeur.sheetnames)

feuille = classeur["Sheet 1"]

print()
print(f"Max row = {feuille.max_row}")
print()

action = input("Que souhaitez-vous faire ?\n1 - Rechercher un prospect\n2 - Ajouter un prospect\n")
print(f"Votre choix : {action}")
print()

if action == "1":

    nom = input("Quel prospect recherchez-vous?")
    trouve = False
    
    for ligne in range(3, feuille.max_row + 1):

        if feuille.cell(row=ligne, column=1).value.lower()  == nom.lower():
            trouve = True 
            print(f"{feuille.cell(row=ligne, column=1).value} - {feuille.cell(row=ligne, column=2).value}")
        
            while True:

                change = input("Voulez-vous changer son budget? Oui/Non : ")

                if change == "Oui":
                    nouveau = int(input("Quel est le nouveau budget? "))
                    feuille.cell(row=ligne, column=2).value = nouveau
                    classeur.save("prospects_immo copy.xlsx")
                    print("Nouveau budget enregistré!")
                    break

                elif change == "Non":
                    print("À très bientôt!")
                    break 
        
                else:
                    print("Entrée incorrecte. Veuillez répondre par Oui ou Non")

    if trouve == False: 
            print("Aucun prospect trouvé. Allez jouer ailleurs! On est occupé ici.")

elif action == "2":

    new_pros = input("Nom du nouveau prospect : ")
    zob = False
    
    for zgeg in range(3, feuille.max_row + 1):
        
        if new_pros.lower() == feuille.cell(row=zgeg, column=1).value.lower() :
            zob = True
            print()
            print("Ce prospect existe déja. Veuillez aller jouer dans le jardin.")
            break

    if zob == False:

        new_budget = int(input("Quel est son budget : "))
        ligne_libre = 3
                        
        while feuille.cell(row=ligne_libre, column=1).value is not None:
            ligne_libre += 1
                        
        feuille.cell(row=ligne_libre, column=1).value = new_pros
        feuille.cell(row=ligne_libre, column=2).value = new_budget
                        
        classeur.save("prospects_immo copy.xlsx")
            
        if new_budget < 300000:
            print("Nouveau prospect ajouté... mais un tocard...")
        else:
            print("Nouveau prospect ajouté ! LET'S MAKE MONEY !!! $$$ ;-) ")
    

    

