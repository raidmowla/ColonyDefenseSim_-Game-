from room import Room

class Courtyard(Room):
	def __init__(self, name):
    		'''
			courtyard room inherited from room class
			'''
		super().__init__(name)
		self.description = """\nYou are in the courtyard of a rimworld colony after surviving a raider attack that has devasted your colony. 
You look at the main colony building. It's seen better days. You remember those days. There's no one left, yet you hear rustling inside the base.
You can go north into the colony building and search for supplies. There's likely gear leftover.
You can go south to inspect and mount the walls. There appears to be turrets along the walls. It looks like the turrets are offline and some are damaged. You also see places where the walls are damaged. 
You should head inside to find supplies to repair the walls and turrets and maybe a way to turn the power back on. 
The raiders will be back, move quickly. 
\n"""
		self.doors = {"n": "entry", "s": "walls"}
		self.contents = []
		self.special = []

	def get_random_enemy(self):
		return None