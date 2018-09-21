#Room list and descriptions imported from txt file
import enemy
import items
####################################################################################################################
# Formats the Enemy and Item classes into the room objects.
def format_class(text):
    """Format text from file into class instances"""

    if "EMPTY" in text:
            return

    # Enemies to be imported from text file and module
    enemies = enemy.enemy_unpack("game_enemy.txt")
    if "EnemyOne" in text:
            return enemies[0]
    if "EnemyTwo" in text:
            return enemies[1]
    if "EnemyThree" in text:
            return enemies[2]
    if "EnemyFour" in text:
            return enemies[3]
    if "EnemyFive" in text:
            return enemies[4]
    if "BossOne" in text:
            return enemies[5]
    if "BossTwo" in text:
            return enemies[6]
    if "BossThree" in text:
            return enemies[7]
    if "BossFour" in text:
            return enemies[8]
    if "BossFive" in text:
            return enemies[9]
    if "FinalBoss" in text:
            return enemies[10]

    # Items to be imported from text file and module
    potions = items.potion_unpack("game_potions.txt")
    weapons = items.weapon_unpack("game_weapons.txt")
    armours = items.armour_unpack("game_armour.txt")
    if "PotionOne" in text:
        return potions[0]
    if "PotionTwo" in text:
        return potions[1]
    if "PotionThree" in text:
        return potions[2]
    if "WeaponOne" in text:
        return weapons[0]
    if "WeaponTwo" in text:
        return weapons[1]
    if "WeaponThree" in text:
        return weapons[2]
    if "WeaponFour" in text:
        return weapons[3]
    if "WeaponFive" in text:
        return weapons[4]
    if "ArmourOne" in text:
        return armour[0]
    if "ArmourTwo" in text:
        return armours[1]
    if "ArmourThree" in text:
        return armours[2]
    if "ArmourFour" in text:
        return armours[3]
    if "ArmourFive" in text:
        return armours[4]
    if "ArmourSix" in text:
        return armours[5]
####################################################################################################################
# Unpacks the game room text file, formatting all the data within, utilising the format class function.
def room_unpack(file):
    """Creating all objects from a text file"""
    with open(file, "r") as f:   
        rooms = []
        for line in f:
            line = line.strip()
            line = line.replace("/", "\n")
            line = line.split("*")
            name = line[0]
            description = line[1]
            items = format_class(line[2])
            enemy = format_class(line[3])

            room = Room(name, description, items, enemy)
            rooms.append(room)
        return rooms
####################################################################################################################
# The Room class.
class Room:
    """All Rooms in the game"""
    def __init__(self, name, description, items, enemy):
        self.name = name
        self.description = description
        self.items = [items]
        self.enemy = enemy

    def __str__(self):
        return "\t{}\n\t************\nDescription: {}\nItems: {}\nEnemy: {}".format(self.name, self.description, self.items, self.enemy)