from room import Room

class DiningRoom(Room):
	def __init__(self, name):
    		'''
			dining room inherited from room class
			'''
		super().__init__(name)
		self.description = """\nYou are in the dining room.\nYou can head north to the barracks, south to the living room, west to the workshop and east to the kitchen.\n"""
		self.contents = []
		self.doors = {"n": "barracks", "s": "lr", "w": "workshop", "e": "kitchen"}
		self.special = []
