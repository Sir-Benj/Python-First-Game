The game should have five python files (enemy.py, items.py, player.py, room.py and Main.py).

It should also include six text files (game_armour.txt, game_enemy.txt, game_map.txt, game_potions.txt, game_room.txt and game_weapons.txt).

Each text file can be modified as follows:

(all numbers to be input as whole integers, no floats.)

game_armour.txt:
-can have up to 6 armours.
-order is name, description, damage reduction amount.
-an asterisk must be included between each different attribute.
-classified from line one to six as ArmourOne to ArmourSix in the game_room.txt file. eg. ArmourOne = the first line of the text file.

game_weapons.txt:
-can have up to 5 weapons.
-order is name, description, attack damage increase.
-an asterisk must be included between each different attribute.
-classified from line one to six as WeaponOne to WeaponFive in the game_room.txt file. eg. WeaponOne = the first line of the text file.

game_potions.txt:
-can have up to 3 potions.
-order is name, description, heal amount.
-an asterisk must be included between each different attribute.
-classified from line one to six as PotionOne to PotionThree in the game_room.txt file. eg. PotionOne = the first line of the text file.

game_enemy.txt:
-can have up to 11 enemies.
-order is name, hp, maxhp, attack damage, heal spell count, heal amount, magic spell count, spell attack damage.
-an asterisk must be included between each different attribute.
-classified from line one to five as EnemyOne to EnemyFive, line six to ten as BossOne to BossFive and line eleven as FinalBoss in the game_room.txt file. eg. EnemyOne = the first line of the text file, BossOne = sixth line of the text file, FinalBoss = line eleven.

game_room.txt:
-can have up to 17 rooms.
-order is name, description, item, enemy.
-an asterisk must be included between each different attribute.
-only one item and enemy per room.
-item can be any item as long as it follows the previously explained notation.
-enemy can be any enemy as long as it follows the previously explained notation.

game_map.txt:
-can have up to 17 rooms.
-each line must start with the corresponding room, e.g, line 1 = room1, line 2 = room2 etc.
-room4, room6, room11 and room15 must be mini-boss rooms (or just contain an enemy of some sort, defeat of these will unlock the final boss room.)
-room16 must lead to room17.
-all other rooms can be connected however you like.
-a space, " " must be included between room names when placed within.
-e.g room1 room4 room8 room16.