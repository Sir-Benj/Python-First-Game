# The Main Game Module
# Ben Harding
####################################################################################################################
# Function to check if the required files to run exist.
import os
import sys
def test_txtf(textfile):
	try:
		tf = open(textfile, "r")
	except IOError:
		print("There was an error opening",textfile,", it does not exist. Cannot run program.")
		input("Press the enter key to exit.")
		exit()
# Function to check if text files are not empty.
def test_lines(textfile):

	if os.stat(textfile).st_size == 0:
		print(textfile,"is missing data. Program cannot run.")
		input("Press enter to exit.")
		exit()
# Testing for the presence of the required textfiles/contents, if not present program exits gracefully.
req_files = ["game_armour.txt","game_weapons.txt","game_room.txt","game_potions.txt","game_map.txt","game_enemy.txt"]		
for file in req_files:
	test_txtf(file)
	test_lines(file)
####################################################################################################################
# Importing the required modules.
import player
import enemy
import items
import room
####################################################################################################################
# Function to format the game map text file into variable names.
def format_vari(line2):
	"""Formats the text file for the map"""
	if line2 == "room1":
	    return room1
	if line2 == "room2":
	    return room2
	if line2 == "room3":
	    return room3
	if line2 == "room4":
	    return room4
	if line2 == "room5":
	    return room5
	if line2 == "room6":
	    return room6
	if line2 == "room7":
	    return room7
	if line2 == "room8":
	    return room8
	if line2 == "room9":
	    return room9
	if line2 == "room10":
	    return room10
	if line2 == "room11":
	    return room11
	if line2 == "room12":
	    return room12
	if line2 == "room13":
	    return room13
	if line2 == "room14":
	    return room14
	if line2 == "room15":
	    return room15
	if line2 == "room16":
	    return room16
	if line2 == "room17":
	    return room17
####################################################################################################################
# Function to open the map file into a dictionary (adjacency list), utilises the format_vari function.
def open_map(text):
    """To open a map from a text file"""
    world_map = {}
    for line in open(text,'r'):
            line2 = line.split()
            room = line2[0]
            room = format_vari(room)
            #print(room)
            room_loc = line2[1:]
            #print(room_loc)
            room_location = []
            for location in room_loc:
                location = format_vari(location)
                #print(location)
                room_location.append(location)

            world_map[room]=room_location

    return world_map
####################################################################################################################
victory = False
game_over = False
game_choice = None

# Initiate the game loop.
while game_choice != "2":
	#Welcome Screen
	print("""
		          )                                    )             
	    (      )\\ )  (        ( /(   ( /(   )\\ )   ( /(   ( /(       
	    )\\    (()/(  )\\))(    )\\())  )\\()) (()/(   )\\())  )\\()) (    
	 ((((_)(   /(_))((_)()\\  ((_)\\  ((_)\\   /(_)) ((_)\\  ((_)\\  )\\   
	  )\\ _ )\\ (_))  (_()((_)__ ((_)   ((_) (_))_|   ((_)  _((_)((_)  
	  (_)_\\(_)| _ \\ |  \\/  |\\ \\ / /  / _ \\ | |_    / _ \\ | \\| || __| 
	   / _ \\  |   / | |\\/| | \\ V /  | (_) || __|  | (_) || .` || _|  
	  /_/ \\_\\ |_|_\\ |_|  |_|  |_|    \___/ |_|     \___/ |_|\\_||___|

	 """)

	print("\t\tFight as a lone Warrior through hordes of enemies,")
	print("\t\t  to get sweet loot and the glory of victory!")
	print("""
			   1 - Start a new game
			   2 - Exit the game
						
	""")
	# Start Game.
	game_choice = input("\t\t\tPlease select an option: ")
	# Begin and check name for errors.
	if game_choice == "1":
		player_name = ""
		while player_name == "":
			player_name = input("\nPlease enter a name for your character: ")
			if len(player_name) > 15:
				print("\nYour name can only be a maximum of 15 characters.")
				player_name = ""
			elif player_name == "":
				print("\nThat is not a valid name, enter another.")

		os.system("cls")
		print("\nYour world begins to shift as you begin to see a vision of a person...")

		# Initiate the Player object.
		player = player.Player(player_name)
		# Get the rooms from text file.
		rooms = room.room_unpack("game_room.txt")
		# Initiate the room objects.
		room1 = rooms[0]
		room2 = rooms[1]
		room3 = rooms[2]
		room4 = rooms[3]
		room5 = rooms[4]
		room6 = rooms[5]
		room7 = rooms[6]
		room8 = rooms[7]
		room9 = rooms[8]
		room10 = rooms[9]
		room11 = rooms[10]
		room12 = rooms[11]
		room13 = rooms[12]
		room14 = rooms[13]
		room15 = rooms[14]
		room16 = rooms[15]
		room17 = rooms[16]
		# Get the world map from file.
		worldmap = open_map("game_map.txt")
		# Start location.
		location = room1
		
        # Initiate main loop of location choice.
		while victory != True or game_over != True:
			print("\nCurrent Location: ",location.name)
			print("\n",player.name,"travels forward...\n", location.description)

			# Initiate attack cycle if enemy is present and alive.
			if isinstance(location.enemy, enemy.Enemy) and location.enemy.is_alive():
				input("\nYou see something out of the corner of your eye...")
				os.system("cls")
				player.attack_cycle(location.enemy)
				
            # Check for victory.
			if location == room17:
				if player.victory(location) == True:
					game_choice = "2"
					break
            # Check for defeat.
			if not player.is_alive():
				player.game_over()
				game_choice = "2"
				break
				
            # Loot and inventory menu.         
			player.inv_loc_menu(location)
			# Next destination choice.
			print("\nCurrent location: ",location.name)
			print("\nCurrent HP:",player.hp)
			print("\nThe areas you can go from here: \n")
			choice=-1
			lim=len(worldmap[location])
			while choice not in range(1, lim+1):
				for (i, place) in enumerate(worldmap[location]):
					print("\n",i + 1, place.name) 
				try:
					choice = int(input("\nChoose where you want to go: "))
					if choice > len(worldmap[location]):
						print("\nThat is outside the range of choices, try again.\n")
					else:
						location = worldmap[location][choice - 1]
				except:
					print("\nThat command was invalid, try again.\n")
				
				# Special condition, if any miniboss alive cannot progress to final boss.
				if location == room17:
					# Checks if mini bosses are alive and blocks path.
					if room4.enemy.is_alive() or room6.enemy.is_alive() or room11.enemy.is_alive() or room15.enemy.is_alive():
						print("\nThe Door remains closed, it appears to be locked by an extremely powerful magic force.")
						print("\nThere must be a way to bring down the barrier within the area...")
						input("\nPress the enter key to go back to the location menu.")
						location = room16
					# Checks if bosses are dead and unlocks path.
					if room4.enemy.is_alive() != True and room6.enemy.is_alive() != True and room11.enemy.is_alive() != True and room15.enemy.is_alive() != True:
						print("\nThe spell lock is broken! The way to the throne room is clear...")
						input("\nPress the enter key to face your final foe...")
						location = room17
					
			os.system("cls")
	        		 

	# Ends the game from the main menu if chosen.
	if game_choice == "2":
		break
