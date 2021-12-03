from room import Room

class LivingRoom(Room):
	def __init__(self, name):
    		'''
			living room inherited from room class
			'''
		super().__init__(name)
		self.description = """\nYou are in a living room.\nThere are chairs and couches scattered around. A fireplace sits unlit.\nYou spot a book shelf, viewscreen, fireplace and a cabinet.\nYou can go north to the dining area or west to the entry.\n"""
		self.doors = {"n": "dining", "w": "entry"}
		self.contents = ["Survival Rifle"]
		self.special = []