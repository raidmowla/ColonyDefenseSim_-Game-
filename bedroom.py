from room import Room

class Barracks(Room):
	def __init__(self, name):
    		'''
			Bed room inherited from room class
			'''	
		super().__init__(name)
		self.description = """\nYou've entered the barracks. There is large pool of blood by one of the bunks.\nBloodied rags, sheets and other clothing lay on and around the bed.\nA reminder of a failure.\n 
		You can head west to the reactor, east to the kitchen and south to the dining area.\n"""
		self.contents = ["Safety Gear"]
		self.special = []

	def get_random_enemy(self):
		return None
