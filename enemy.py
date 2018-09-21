# Enemy Class
# Creating as a module.
# Creating the Enemy Class.
class Enemy:
    """For Each Enemy in the game"""
    def __init__(self, name, hp, maxhp, attack, heal_count, heal, magic_count, magic_attack):
    	self.name=name
    	self.hp=hp
    	self.maxhp=maxhp
    	self.attack=attack
    	self.heal_count=heal_count
    	self.heal=heal
    	self.magic_count=magic_count
    	self.magic_attack=magic_attack

    def __str__(self):
        return "\t{}\n***********\nHP:{}\nMaxHP:{}\nAttack:{}\nHeal Count:{}\nHeal:{}\nMagic Count:{}\nMagic Attack:{}".format(self.name, self.hp, self.maxhp, self.attack, self.heal_count, self.heal, self.magic_count, self.magic_attack)

    def is_alive(self):
        return self.hp > 0
####################################################################################################################
# Function to unpack the enemy text file and create Enemy class objects to append to a list.
def enemy_unpack(file):
    """Creating all enemies from a text file"""
    with open(file, "r") as f:
        enemies = []
        for line in f:
            line = line.strip()
            line = line.replace("/", "\n")
            line = line.split("*")

            name = line[0]
            hp = int(line[1])
            maxhp = int(line[2])
            attack = int(line[3])
            heal_count = int(line[4])
            heal = int(line[5])
            magic_count = int(line[6])
            magic_attack = int(line[7])

            enemy = Enemy(name, hp, maxhp, attack, heal_count, heal, magic_count, magic_attack)
            enemies.append(enemy)
        return enemies