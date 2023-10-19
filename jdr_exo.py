import random
import time
time.sleep(0.5)

#pv_user = int(50)
#pv_png = int(50)



boss_choices = "\nGobilinous le gobelin? (1)\nArchos le sentinel? (2)\nBalrog des enfer!? (3)\n---> "

menu_choices1 = ["1","2","3"]

hero_choice = "\n\n--->"

menu = "Attaque (1) --- Potion (2)   :       "

menu_choices = ["1","2"]

menu_choices1 = ["1","2","3"]




print("°°° ENTRE DANS L'ARENE !!!! °°° ")
time.sleep(1)
print("°°° TON ADVERSAIRE SERAAAAA .....")
time.sleep(1.2)

while True:

    user_choice = ""
    while user_choice not in menu_choices1:
        user_choice = input(boss_choices)
        if user_choice not in menu_choices1:
            print(f"{user_choice} est invalide")

    if user_choice == "1":
        pv_png = 40
        att_png = 6  

    if user_choice == "2":
        pv_png = 60
        att_png = 9 

    elif user_choice == "3":
        pv_png = 100
        att_png = 15 

        break
    break




 
time.sleep(1)

print("Quel hero va tu envoyé à la mort ?..\n")
time.sleep(1)
print("Le chevalier des limbes..(1)\n°70 PV\n°10 ATT\n°2 potions\n")
time.sleep(0.5)
print("Le mage des sables..(2)\n°85 PV\n°7 ATT\n°3 potions\n")
time.sleep(0.5)
print("La moine lunaire..(3)\n°45 PV\n°14 ATT\n°4potions\n")
time.sleep(0.5)


while True:

    user_choice = ""
    while user_choice not in menu_choices1:
        user_choice = input(hero_choice)
        if user_choice not in menu_choices1:
            print(f"{user_choice} est invalide")

    if user_choice == "1":      #Chevalier
        pv_user = 70
        att_user = 10
        potions = 2

    if user_choice == "2":      #Mage
        pv_user = 70
        att_user = 7
        potions = 3

    elif user_choice == "3":    #Moine
        pv_user = 45
        att_user = 14
        potions = 4

        break
    break
        



time.sleep(1)
print("PRET ?!")
time.sleep(1)
print("-~-"*35)
time.sleep(0.4)

 



while True:

    user_choice = ""
    if pv_png and pv_user <=0:
        print("       Match nul...")
        break

    if pv_user <=0:
        print("    GAME OVER    ")
        break

    if pv_png <=0:
        print("    BRAVISSIMO GRINGO T'ES LE BOSS      ")
        break

    while user_choice not in menu_choices:
        user_choice = input(menu)

        if user_choice not in menu_choices:
            print(f"{user_choice} est invalide")

        

        if user_choice == "1":
            r_png = random.randint(1,4)
            r_user = random.randint(2,5)
            pv_user -= int(att_png) + int(r_png)
            pv_png -= int(att_user) + int(r_user)

            print(f"\nVous avez infligé {att_user+r_user} dégats\u2694\uFE0F.")  
            print(f'Vous avez subi {att_png+r_png} dégats\u2694\uFE0F.\n')
            print("\u2764\uFE0F"+f"  Vos pv : {pv_user}")
            print("\u2763\uFE0F"+f"  Les siens : {pv_png}.")

        if user_choice == "2":
            if potions ==0:
                print("Vous n'avez plus de potions !")
                break

            elif potions !=0:
                potions -= 1
            r_png= random.randint(5, 15)
            value_potion = random.randrange(15, 30, 5)
            pv_user += value_potion
            pv_user -= int(att_png) + int(r_png)

            print(f"""Vous gagné {value_potion} PV !
Il vous restes {potions} potions 🧪""")
            
            if potions <= 1:
                print("Pas terrible...")

            else:
                print("Plutôt cool !!")

            print(f"Vous subissez {att_png+r_png} dégats\u2694\uFE0F.")
            print("\u2764\uFE0F"+f"   Vos PV : {pv_user}")
            print("\u2763\uFE0F"+f"   Les siens : {pv_png}")

            skip_turn = True
        


           
    
    
    print(" ")
    print("-~-"*35)      
    print(" ")
    
