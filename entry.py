from room import Room

class EntryWay(Room):
	def __init__(self, name):
    		'''
			entryway room inherited from class room
			'''
		super().__init__(name)
		self.description = """\nYou step inside the colony's main entryway. There are opened boxes scattered about the hallway. 
They might contain something.Blood streaks lead north into the workshop.\n
You can head west into the armory, east to the living room and north to the workshop. 
		\n"""
		self.contents = ["Knife"]
		self.doors = {"n": "workshop", "e": "lr", "w": "armory", "s": "courtyard"}
		self.special = []
		
	def get_random_enemy(self):
		return None