from room import Room


class Armory(Room):
	def __init__(self, name):
    		'''
			Armory room inherited from room class
			'''	
		super().__init__(name)
		self.description = """\nThe door slides open and you step inside the armory. 
		Most of the equipment and weapons are gone.
		You spot a few lockers and boxes left untouched. 
		You can go north to the workshop or head east to the entry way. 
		\n"""
		self.contents = [".45 Automatic Pistol", "Turret Components"]
		self.doors = {"n": "workshop", "e": "entry"}
		self.special = []