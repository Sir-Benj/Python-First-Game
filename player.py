# Player Class
# Creating as a module.
# Importing modules to use.
import random
import os
import enemy
import items
import room
####################################################################################################################
# Unpack weapon armour and enemy classes for use in the module.
weapons = items.weapon_unpack("game_weapons.txt")
armours = items.armour_unpack("game_armour.txt")
enemies = enemy.enemy_unpack("game_enemy.txt")
####################################################################################################################
# The Player Class.
class Player(object):
    """The Player Character"""

    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.weapon = weapons[0]
        self.armour = armours[0]
        self.hp = 200
        self.maxhp = 200
        self.attack = 10        
        self.heal = 50
        self.heal_count = 5
        self.magic_attack = 50
        self.magic_count = 5

    def __str__(self):
        return "\t{}\n\t************\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n".format(self.name, self.inventory, self.weapon, self.armour, self.hp, self.attack, self.heal, self.heal_count)

    def is_alive(self):
        return self.hp > 0
####################################################################################################################
# The Victory function, tests when the player has won the game.
    def victory(self, location):
            if location.enemy.is_alive() != True:
                os.system("cls")
                print("""
                       _   _ _____ _____ _____ _____________   __              
                      | | | |_   _/  __ |_   _|  _  | ___ \\ \\ / /              
                      | | | | | | | /  \\/ | | | | | | |_/ /\\ V /               
                      | | | | | | | |     | | | | | |    /  \\ /                
                      \\ \\_/ /_| |_| \\__/\\ | | \\ \\_/ | |\\ \\  | |                
                       \\___/ \\___/ \\____/ \\_/  \\___/\\_| \\_| \\_/                
                                                                               
                                                                           
        __   __            _   _                   _    _               _  
        \\ \\ / /           | | | |                 | |  | |             | | 
         \\ V /___  _   _  | |_| | __ ___   _____  | |  | | ___  _ __   | | 
          \\ // _ \\| | | | |  _  |/ _` \\ \\ / / _ \\ | |/\\| |/ _ \\| '_ \\  | | 
          | | (_) | |_| | | | | | (_| |\\ V |  __/ \\  /\\  | (_) | | | | |_| 
          \\_/\\___/ \\__,_| \\_| |_/\\__,_| \\_/ \\___|  \\/  \\/ \\___/|_| |_| (_) 
            """
            )

                input("\tCongratulations, press the enter key to exit.")
                victory = True
                return victory
            else:
                pass
####################################################################################################################
# The Game Over function, shown after the player has been defeated.
    def game_over(self):
        print("""
             _____   ___  ___  ___ _____   _____  _   _ ___________ 
            |  __ \\ / _ \\ |  \\/  ||  ___| |  _  || | | |  ___| ___ \\
            | |  \\// /_\\ \\| .  . || |__   | | | || | | | |__ | |_/ /
            | | __ |  _  || |\\/| ||  __|  | | | || | | |  __||    / 
            | |_\\ \\| | | || |  | || |___  \\ \_/ /\\ \_/ / |___| |\\ \\ 
             \\____/\\_| |_/\\_|  |_/\\____/   \\___/  \\___/\\____/\\_| \\_|
        """
        )
        input("\t\tPress the enter key to exit.")
        os.system("cls")
####################################################################################################################
    # Looting function, allows for the display, selection and allocation of items.
    def looting(self, location):
        print("\nYou find something you can use.")
        print("\nYou can take:\n ")
        # Check if any items present at location.
        items_ava = []
        for item in location.items:
            if isinstance(item, items.Items):
                items_ava.append(item)
            else:
                pass
        # Make loot selectable.
        loot_choice = -1
        lim = len(items_ava)
        while loot_choice not in range(1, lim+1):
            for (i, item) in enumerate(items_ava):
                print(i+1, item.name)
            try:
                loot_choice = int(input("\nChoose what item to take or enter '0' to exit the menu: "))
                if loot_choice == 0:
                    break

                elif loot_choice > len(items_ava):
                    print("\nThat is outside the range of choices, try again.\n")
                # Place loot in inventory and remove from room.
                elif loot_choice in range(1, lim+1):
                    print("\n", items_ava[loot_choice-1].name,"has been added to your inventory.")
                    self.inventory.append(items_ava[loot_choice-1])
                    location.items.remove(items_ava[loot_choice-1])
            except:
                print("\nThat command is invalid, try again.\n")
####################################################################################################################
    # Player inventory menu and equipment manager
    def inv_manage(self):
        """Inventory Management For The Player"""
        choice = -1
        while choice != "5":
            print("""
                        Inventory

                1 - View Inventory.
                2 - Remove Item From Inventory.
                3 - Equip Weapon.
                4 - Equip Armour.
                5 - Exit Menu.

                """
                )
            choice = input("Please choose an option: ")
            # Shows the inventory.
            if choice == "1":
                if len(self.inventory) == 0:
                    print("\nYour inventory is empty.")
                else:
                    print("\nThis is your inventory:\n ")
                    for item in self.inventory:
                        print("\n",item)
            # Displays all items in inventory and allows selection.
            if choice == "2":
                inv_choice = -1
                lim = len(self.inventory)
                while inv_choice not in range(1, lim+1):
                    if len(self.inventory) == 0:
                        print("\nYour inventory is empty.")
                        break

                    print("\nInventory:\n ")
                    for (i, item) in enumerate(self.inventory):
                        print("\n", i+1, item)

                    try:
                        inv_choice = int(input("\nChoose what item to remove or enter '0' to exit the menu: "))
                    
                        if inv_choice == 0:
                            break

                        elif inv_choice > len(self.inventory) and len(self.inventory) != 0:
                            print("\nThat is outside the range of choices, try again.\n")
                        # Removes from inventory.
                        elif inv_choice in range(1, lim+1):
                            print("\n", self.inventory[inv_choice-1],"has been removed from your inventory.")
                            del self.inventory[inv_choice-1]
                    except:
                        print("\nThat command is invalid, try again.\n")
            # Show weapon equipped in weapon slot and weapons that can be equipped from the player inventory.
            if choice == "3":
                weapon_check = []
                # Checks for weapons in inventory.
                for item in self.inventory:
                    if isinstance(item, items.Weapons):
                        weapon_check.append(item)
    
                if len(weapon_check) > 0:
                    print("\nCurrently Equipped Weapon:\n",self.weapon)
                    print("\nWhich weapon would you like to equip?")
                    print("\nYou can equip: ")
                    weapon_ava = []
                    for item in self.inventory:
                        if isinstance(item, items.Weapons):
                            weapon_ava.append(item)
                        else:
                            pass
                    # Displays weapons for selection.
                    lim = len(weapon_ava)
                    weapon_choice = -1
                    while weapon_choice not in range(1, lim+1):
                        for (i, item) in enumerate(weapon_ava):
                            print("\n",i+1, item,"\n")
                            
                        try:
                            weapon_choice = int(input("\nChoose a weapon to equip or enter '0' to exit the menu: "))
                            os.system("cls") 
                            if weapon_choice == 0:
                                break

                            elif weapon_choice > len(weapon_ava):
                                print("\nThat is outside the range of choices, try again.\n")
                            # Adds weapon to slot, if a weapon is already present puts that back in the player inventory.
                            elif weapon_choice in range(1, lim+1):
                                print("\n",weapon_ava[weapon_choice-1].name,"...has been added to your weapon slot.")
                                if isinstance(self.weapon, items.Weapons):
                                    self.inventory.append(self.weapon)
                                if self.weapon == None:
                                    print("\nThere was nothing in your weapon slot to add back to the inventory.")
                                else:
                                    print("\n",self.weapon.name,"...has been added to your inventory.")
                                self.weapon = weapon_ava[weapon_choice-1]
                                self.inventory.remove(weapon_ava[weapon_choice-1])
                        except:
                            print("\nThat command is invalid, try again.\n")

                else:
                    print("\nThere are no weapons in your inventory.")
            # Show armour equipped in armour slot, and armour that can be equipped from the player inventory.
            if choice == "4":
                armour_check = []
                # Checks for armour in inventory.
                for item in self.inventory:
                    if isinstance(item, items.Armour):
                        armour_check.append(item)
    
                if len(armour_check) > 0:
                    print("\nCurrently Equipped Armour:\n", self.armour)
                    print("\nWhich piece of armour would you like to equip?")
                    print("\nYou can equip: ")
                    armour_ava = []
                    for item in self.inventory:
                        if isinstance(item, items.Armour):
                            armour_ava.append(item)
                        else:
                            pass
                    # Display armour for selection.
                    lim = len(armour_ava)
                    armour_choice = -1
                    while armour_choice not in range(1, lim+1):
                        for (i, item) in enumerate(armour_ava):
                            print("\n",i+1, item,"\n")
                            
                        try:
                            armour_choice = int(input("\nChoose an armour to equip or enter '0' to exit the menu: "))
                            os.system("cls")

                            if armour_choice == 0:
                                break

                            if armour_choice > len(armour_ava):
                                print("\nThat is outside the range of choices, try again.\n")
                            # Adds armour to slot, if armour is already present puts that back in the player inventory.
                            elif armour_choice in range(1, lim+1):
                                print("\n", armour_ava[armour_choice-1].name,"...has been added to your armour slot.")
                                if isinstance(self.armour, items.Armour):
                                    self.inventory.append(self.armour)
                                if self.armour == None:
                                    print("\nThere was nothing in your armour slot to add back to the inventory.")
                                else:
                                    print("\n",self.armour.name,"...has been added to your inventory.")
                                self.armour = armour_ava[armour_choice-1]
                                self.inventory.remove(armour_ava[armour_choice-1])

                        except:
                            print("\nThat command is invalid, try again.\n")

                else:
                    print("\nThere is no armour in your inventory.")

####################################################################################################################
    # Location menu, designed for healing in between battles and accessing other menus
    def inv_loc_menu(self, location):
        inv_loc_choice = -1
        while inv_loc_choice != "1":
            print ("\nLocation Menu: ")
            print("""
                1 - Choose the next location.
                2 - Check for items at this location.
                3 - Manage your inventory.
                4 - Heal yourself using spells.
                5 - Heal yourself using a potion.
                """
            )
            print("Current HP:",self.hp)
            print("Current Healing Spell Count:",self.heal_count)

            inv_loc_choice = input("\nWhat would you like to do? ")
            # checks if any item objects present at location, if there are, starts the looting function.
            if inv_loc_choice == "2":
                for item in location.items:
                    if isinstance(item, items.Items):
                        self.looting(location)
                else:
                    print("\nThere is nothing else to take here.")
            # Starts inventory manangement function.
            elif inv_loc_choice == "3":
                self.inv_manage()
            # Starts self healing function.
            elif inv_loc_choice == "4":
                if self.heal_count == 0:
                    print("\nYou can't cast anymore heals.")

                if self.hp == self.maxhp:
                    print("\nYou are at max hp.")
                    break    
                # Starts loop of healing.
                heal_choice = input("\nWould you like to use a spell to heal? 1=yes, 2=no: ")
                while heal_choice != "2": 
                    if heal_choice == "1":
                        self.hp += (self.heal + random.randint(1, 10))
                        if self.hp > self.maxhp:
                            print("\nYou have been healed to max hp.")
                            self.hp = 200
                            self.heal_count -= 1
                            break

                        elif self.hp < self.maxhp:
                                print("\nYou heal for",self.heal,"health points, you currently have",self.hp,"health points.\n")
                                self.heal_count -= 1
                                heal_choice = input("\nWould you like to use a spell to heal again? 1=yes, 2=no: ")

                        elif self.heal_count == 0:
                            print("\nYou can't cast anymore heals.")

                    else:
                        print("\nThat command was invalid, try again.")
                        heal_choice = input("\nWould you like to use a spell to heal again? 1=yes, 2=no: ")
            # Using a healing potion to heal the player.      
            elif inv_loc_choice == "5":
                potion_check = []
                # Check for healing potions in inventory.
                for item in self.inventory:
                    if isinstance(item, items.Potions):
                        potion_check.append(item)

                if len(potion_check) > 0: 
                    print("\nYour Current HP: ",self.hp)
                    print("\nYou can use these potions: \n")
                    potion_ava = []
                    for item in self.inventory:
                        if isinstance(item, items.Potions):
                            potion_ava.append(item)
                        else:
                            pass
                    lim = len(potion_ava)
                    potion_choice = -1
                    if lim > 0:
                        # Display potions for selection.
                        while potion_choice not in range(1, lim+1):
                            for (i, item) in enumerate(potion_ava):
                                print("\n",i+1, item.name,"\n")
                            potion_choice = int(input("\nChoose a potion to use or enter '0' to exit to the location menu: "))
                            os.system("cls")
                            if potion_choice == 0:
                                break
                            elif potion_choice in range(1, lim+1):
                                print("\n",potion_ava[potion_choice-1].name,"...has been selected.")
                                print("\n",potion_ava[potion_choice-1].name,"heals you for up to",potion_ava[potion_choice-1].heal)
                                # Potion heals player.
                                self.hp += potion_ava[potion_choice-1].heal
                                # Heal can only go to maxhp level.
                                if self.hp > self.maxhp:
                                    self.hp = self.maxhp
                                    self.inventory.remove(potion_ava[potion_choice-1])
                                # Removes potion from inventory.
                                else:
                                    self.inventory.remove(potion_ava[potion_choice-1])
                                print("\nYour HP is now: ",self.hp)
                elif len(potion_check) == 0:
                    print("\nThere are no potions in your inventory.")
####################################################################################################################
    # Attack cycle, player and enemy, turn based
    def attack_cycle(self, enemy):
        """The Attack Cycle For Player And Enemy"""
        if enemy.is_alive() == True:

            print("\nDefeat the enemy",enemy.name,"before they defeat you!")
            turn = random.randint(1,2)
            if turn == 1:
                print("\nYou have the initiative and attack first!\n")
            elif turn == 2:
                print("\nThe enemy",enemy.name,"surprises you and attacks first.!\n")
            while self.is_alive() and enemy.is_alive():

                if turn == 1:
                    print("\nBattle Menu: ")
                    print("""
                1 - Attack ferociously with your weapon.
                2 - Call upon your magic to heal your wounds.
                3 - Call upon your dark magic. Does more damage the lower health the enemy has.
                4 - Use a potion from your inventory.
                        """
                        )
                    print("Your current HP is:",self.hp)
                    print("You have",self.heal_count,"heals remaining.")
                    print("You have",self.magic_count,"spells remaining.")
                    choice = input("\nWhat do you do? ")
                    os.system("cls")                                       

                    # Basic Attack with weapon bonus, 
                    if choice == "1":

                        attack = (self.attack + random.randint(1, 10))
                        full_attack = (attack + self.weapon.attack)
                        enemy.hp -= full_attack
                        print("\nYou strike",enemy.name,"for", full_attack,"damage!\n")
                        # Returns enemy hp, not directly but obfuscated.
                        if enemy.maxhp*0.60 <= enemy.hp <= enemy.maxhp*0.75:
                            print("\n",enemy.name,"has taken light damage.")
                        elif enemy.maxhp*0.35 <= enemy.hp <= enemy.maxhp*0.599:
                            print("\n",enemy.name,"looks wounded.")
                        elif enemy.maxhp*0.01 <= enemy.hp <= enemy.maxhp*0.349:
                            print("\n",enemy.name,"The enemy looks severely wounded.")
                        turn = 2
                   	
                   	# Player Heal                                           
                    elif choice == "2":

                        if self.heal_count == 0:
                            print("\nYou can't cast anymore heals.")

                        elif self.heal_count > 0:
                            self.hp += (self.heal + random.randint(1, 10))
                            if self.hp > self.maxhp:
                                print("\nYou cannot heal beyond your maximum health")
                                print("Health restored to full.")
                                self.hp = 200
                                turn = 2
                                self.heal_count -= 1
                            elif self.hp < self.maxhp:
                                print("\nYou heal for",self.heal,"health points, you currently have",self.hp,"health points.\n")
                                self.heal_count -= 1
                                turn = 2
                        
                    # Player magic attack, does more damage the lower enemy hp is
                    elif choice == "3":

                        if self.magic_count == 0:
                            print("\nYou can't cast any more spells.")
                        # Checks for different levels of enemy health, based on percentage. The lower the enemy hp the higher the damage done.
                        elif self.magic_count > 0:
                            if enemy.maxhp*0.75 <= enemy.hp <= enemy.maxhp:
                                mag_dmg = round((self.magic_attack+random.randint(1,5))*0.5)
                                enemy.hp -= mag_dmg
                                print("\nYour magic is less effective, hitting for",mag_dmg,"damage.\n")
                                self.magic_count -= 1
                                turn = 2
                            elif enemy.maxhp*0.35 <= enemy.hp <= enemy.maxhp*0.75:
                                mag_dmg = self.magic_attack+random.randint(5,10)
                                enemy.hp -= mag_dmg
                                print("\nYour magic is powerful, hitting for",mag_dmg,"damage.\n")
                                self.magic_count -= 1
                                turn = 2
                            elif enemy.maxhp*0.01 <= enemy.hp <= enemy.maxhp*0.35:
                                mag_dmg = round((self.magic_attack+random.randint(10,15))*1.25)
                                enemy.hp -= mag_dmg
                                print("\nYour magic is devastating, hitting for",mag_dmg,"damage.\n")
                                self.magic_count -= 1
                                turn = 2
                            # Returns the enemy health, not directly but obfuscated. 
                            if enemy.maxhp*0.6 <= enemy.hp <= enemy.maxhp*0.75:
                            	print("\n",enemy.name,"has taken light damage.")
                            elif enemy.maxhp*0.35 <= enemy.hp <= enemy.maxhp*0.6:
                            	print("\n",enemy.name,"looks wounded.")
                            elif enemy.maxhp*0.01 <= enemy.hp <= enemy.maxhp*0.35:
                            	print("\n",enemy.name,"The enemy looks severely wounded.")

                    # Use a Potion
                    elif choice == "4":

                        print("\nYou can use these Potions in battle: ")
                        potion_ava = []
                        # Check for potions in inventory.
                        for item in self.inventory:
                            if isinstance(item, items.Potions):
                                potion_ava.append(item)
                            else:
                                pass
                        lim = len(potion_ava)
                        potion_choice = -1
                        if lim == 0:
                            print("\nYou have no potions to use.")
                        elif lim > 0:
                            # Display potions in inventory.
                            while potion_choice not in range(1, lim+1):
                                for (i, item) in enumerate(potion_ava):
                                    print("\n",i+1, item.name)
                                potion_choice = int(input("\nChoose a potion to use or enter '0' to exit to the battle menu: "))
                                os.system("cls")
                                if potion_choice == 0:
                                    break
                                elif potion_choice in range(1, lim+1):
                                    print("\n",potion_ava[potion_choice-1].name,"...has been selected.")
                                    print("\n",potion_ava[potion_choice-1].name,"heals you for",potion_ava[potion_choice-1].heal)
                                    self.hp += potion_ava[potion_choice-1].heal
                                    # Heal only to maxhp and set health to maxhp value and remove selection from inventory.
                                    if self.hp > self.maxhp:
                                        self.hp = self.maxhp
                                        self.inventory.remove(potion_ava[potion_choice-1])
                                        turn = 2
                                    # Heal and remove selection from inventory.
                                    else:
                                        self.inventory.remove(potion_ava[potion_choice-1])
                                        turn = 2
                                
                    else:
                        print("\nThat command is invalid, try again.\n")

                elif turn == 2:

                	# Enemy takes a random move
                    rand_move = random.randint(1,3)
                    # Enemy takes a basic attack
                    if rand_move == 1:

                        en_attack = (enemy.attack + random.randint(1, 10))
                        en_full_attack = (en_attack - self.armour.reduction)
                        if en_full_attack <= 0:
                            en_full_attack = 0
                            self.hp -= en_full_attack
                            print("\n",enemy.name,"attacks but your defense is too strong and it does",en_full_attack,"damage!")
                        else:
                            self.hp -= en_full_attack
                            print("\n",enemy.name," attacks and strikes you for",en_full_attack,"points of damage.")
                        turn = 1
                    # Enemy heals, if cant heal then magic attack, if cant magic attack basic attack
                    if rand_move == 2:

                        if enemy.heal_count >= 1 and enemy.hp < enemy.maxhp*0.5:
                            enemy.hp += enemy.heal
                            print("\n",enemy.name,"heals for",enemy.heal,"!")
                            enemy.heal_count -= 1
                            turn = 1
                        elif enemy.heal_count == 0:
                            if enemy.magic_count >= 1:
                                en_mag_attack = (enemy.magic_attack + random.randint(5, 15))
                                en_fmag_attack = (en_mag_attack - self.armour.reduction)
                                self.hp -= en_fmag_attack
                                print("\n",enemy.name,"attacks with a magic spell for",en_fmag_attack,"points of damage.")
                                turn = 1
                            elif enemy.magic_count == 0:
                                en_attack = (enemy.attack + random.randint(1, 10))
                                en_full_attack = (en_attack - self.armour.reduction)
                                if en_full_attack <= 0:
                                    en_full_attack = 0
                                    self.hp -= en_full_attack
                                    print("\n",enemy.name,"attacks but your defense is too strong and it does",en_full_attack,"damage!")
                                else:
                                    self.hp -= en_full_attack
                                    print("\n",enemy.name,"attacks and strikes you for",en_full_attack,"points of damage.")
                                turn = 1
                    # Enemy magic attack, if can't magic attack, then basic attack
                    if rand_move == 3:

                        if enemy.magic_count >= 1:
                            en_mag_attack = (enemy.magic_attack + random.randint(5, 15))
                            en_fmag_attack = (en_mag_attack - self.armour.reduction)
                            self.hp -= en_fmag_attack
                            print("\n",enemy.name,"attacks with a magic spell for",en_fmag_attack,"points of damage.")
                            turn = 1
                        elif enemy.magic_count == 0:
                            en_attack = (enemy.attack + random.randint(1, 10))
                            en_full_attack = (en_attack - self.armour.reduction)
                            if en_full_attack <= 0:
                                en_full_attack = 0
                                self.hp -= en_full_attack
                                print("\n",enemy.name," attacks but your defense is too strong and it does",en_full_attack,"damage!")
                            else:
                                self.hp -= en_full_attack
                                print("\n",enemy.name,"attacks and strikes you for",en_full_attack,"points of damage.")
                            turn = 1
            # Check if enemy alive
            if enemy.is_alive() != True:
                print("\nYou have slain the enemy!\n")
                self.heal_count=5
                self.magic_count=5
                print("\nYour magic and healing spell count is restored to maximum.")
            # Check if player alive                                                   
            if self.is_alive() != True:
                print("\n\t\tYou have died.")
        # Pass if enemy is dead
        if enemy.is_alive() == False:
            pass