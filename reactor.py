from room import Room
import sys

class Reactor(Room):
    
	def __init__(self, name):
    		'''
			Reactor room inherited from room class
			'''	
		super().__init__(name)
		self.description = """\nAs you walk into the base's reactor room, you feel the electrical discharge in the air.
	You see that base's reactor was damaged during the last raid, 
	likely an overload due to the EMP damage to turrets on the south wall.
	Repairing the reactor will bring power back online.\n
	You can head east to the barracks or south to the workshop.\n"""
		self.contents = []
		self.special = ["Base Reactor"]
		self.doors = {"e": "barracks", "s": "workshop"}
