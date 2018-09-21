# Items Class, creating all items from text files
# Creating to save as a module
####################################################################################################################
# Unpacks the potion text file into Potion class objects and appends them to a list.
def potion_unpack(file):
    """Creating all potions from a text file"""
    with open(file, "r") as f:
        potions = []
        for line in f:
            line = line.strip()
            line = line.replace("/", "\n")
            line = line.split("*")

            name = line[0]
            description = line[1]
            heal = int(line[2])

            potion = Potions(name, description, heal)
            potions.append(potion)
        return potions
# Unpacks the weapons text file into Weapon class objects and appends them to a list.
def weapon_unpack(file):
    """Creating all weapons from a text file"""
    with open(file, "r") as f:
        weapons = []
        for line in f:
            line = line.strip()
            line = line.replace("/", "\n")
            line = line.split("*")
            name = line[0]
            description = line[1]
            attack = int(line[2])

            weapon = Weapons(name, description, attack)
            weapons.append(weapon)
        return weapons
# Unpacks the armour text file into Armour class objects and appends them to a list.
def armour_unpack(file):
    """Creating all armour from a text file"""
    with open(file, "r") as f:
        armours = []
        for line in f:
            line = line.strip()
            line = line.replace("/", "\n")
            line = line.split("*")
            name = line[0]
            description = line[1]
            reduction = int(line[2])

            armour = Armour(name, description, reduction)
            armours.append(armour)
        return armours
####################################################################################################################
# The Items Class.
class Items:
    """For all the items in the game"""

    def __init__(self, name, description,):
        self.name = name
        self.description = description
# The Potions Subclass.
class Potions(Items):
    """All Potions"""
    def __init__(self, name, description, heal):
        self.name = name
        self.description = description
        self.heal = heal

    def __str__(self):
    	return "\t{}\n\t************\n{}\nHeal: {}\n".format(self.name, self.description, self.heal)
# The Weapons Subclass.
class Weapons(Items):
    """All Weapons"""
    def __init__(self, name, description, attack):
        self.name = name
        self.description = description
        self.attack = attack

    def __str__(self):
        return "\t{}\n\t********\n{}\nAttack: {}\n".format(self.name, self.description, self.attack)
# The Armour Subclass.
class Armour(Items):
    """All Armour"""
    def __init__(self, name, description, reduction):
        self.name = name
        self.description = description
        self.reduction = reduction

    def __str__(self):
        return "\t{}\n\t**************\n{}\nArmour: {}\n".format(self.name, self.description, self.reduction)