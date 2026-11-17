import openpyxl

classeur = openpyxl.load_workbook("prospects_immo copy.xlsx")

print(classeur.sheetnames)

feuille = classeur["Sheet 1"]

print()
print(f"Max row = {feuille.max_row}")
print()

continuer = True

while continuer == True:   
    
    action = input("Que souhaitez-vous faire ?\n1 - Rechercher un prospect\n2 - Ajouter un prospect\n3 - Supprimer un prospect\n4 - Afficher tous les prospects\n5 - Quitter\n")
    print(f"Votre choix : {action}")
    print()

    if action == "1":

        nom = input("Quel prospect recherchez-vous?")
        trouve = False
    
    
        for ligne in range(3, feuille.max_row + 1):

            nom_excel = feuille.cell(row=ligne, column=1).value

            if nom_excel is not None and nom_excel.lower() == nom.lower():
                trouve = True 
                print(f"{feuille.cell(row=ligne, column=1).value} - {feuille.cell(row=ligne, column=2).value}")
        
                while True:

                    change = input("Voulez-vous changer son budget? Oui/Non : ")

                    if change.lower() == "Oui".lower():
                        nouveau = int(input("Quel est le nouveau budget? "))
                        feuille.cell(row=ligne, column=2).value = nouveau
                        classeur.save("prospects_immo copy.xlsx")
                        print("Nouveau budget enregistré!")
                        break

                    elif change.lower() == "Non".lower():
                        print("À très bientôt!")
                        break
        
                    else:
                        print("Entrée incorrecte. Veuillez répondre par Oui ou Non")

        if trouve == False: 
                print("Aucun prospect trouvé. Allez jouer ailleurs! On est occupé ici.")
                continuer = False
                break

    elif action == "2":

        new_pros = input("Nom du nouveau prospect : ")
        zob = False
        
    
        for zgeg in range(3, feuille.max_row + 1):
        
            if feuille.cell(row=zgeg, column=1).value is not None and new_pros.lower() == feuille.cell(row=zgeg, column=1).value.lower()  :
                zob = True
                print()
                print("Ce prospect existe déja. Veuillez aller jouer dans le jardin!")
                print()
                break

        if zob == False:

            while True:
                try:
                    new_budget = int(input("Quel est son budget : "))
                    break
                except ValueError:
                    print("Tu dois entrer un nombre !")
            
            ligne_libre = 3
                        
            while feuille.cell(row=ligne_libre, column=1).value is not None:
                ligne_libre += 1
                        
            feuille.cell(row=ligne_libre, column=1).value = new_pros
            feuille.cell(row=ligne_libre, column=2).value = new_budget
                        
            classeur.save("prospects_immo copy.xlsx")
            if new_budget < 300000:
                print("Nouveau prospect ajouté... mais un tocard...")
                print()
            
            else:
                print("Nouveau prospect ajouté ! LET'S MAKE MONEY !!! $$$ ;-) ")
                
    
    elif action == "3":

        delete = input("Quel prospect supprimer ?")
        trouvee = False
        
        for ligne in range(3, feuille.max_row + 1):

            zboub = feuille.cell(row=ligne, column=1).value
            thune = feuille.cell(row=ligne, column=2).value
            
            if zboub is not None and zboub.lower() == delete.lower():
                trouvee = True
                print(f"Prospect trouvé : {zboub} - {thune}") 
                print()
                
                while True:

                    deletion = input("Confirmer la suppression ? Oui/Non :")

                    if deletion.lower() == "Oui".lower():
                        feuille.delete_rows(ligne)
                        classeur.save("prospects_immo copy.xlsx")
                        break

                    elif deletion.lower() == "Non".lower():
                        print("Ok, mais j'ai pas que ça à faire moi")
                        break

                    else:
                        print()
                        print("Veuillez entrer Oui ou Non")
                
                break

        if trouvee == False: 
            print("Aucun prospect trouvé. Allez jouer ailleurs! On est occupé ici.")

    elif action == "4":
        
        for i in range(3, feuille.max_row + 1):
            if feuille.cell(row=i, column=1).value:
                print(f"{feuille.cell(row=i, column=1).value} - {feuille.cell(row=i, column=2).value}")
        
        while True:
            suite = input("Souhaitez-vous faire autre chose ? Oui/Non: ")
            
            if suite.lower() == "oui".lower():
                break

            elif suite.lower() == "non".lower():
                print("Dégagez alors ! Et rapido !")
                print()
                continuer = False
                break
            
            else:
                print("Veuillez répondre par Oui ou Non")

    elif action == "5":
        print("À bientôt !")
        break

    else:
        print("Choix invalide. Veuillez répondre par: 1, 2 ou 3")
        print()

print("À très bientôt mon chat...")
    

