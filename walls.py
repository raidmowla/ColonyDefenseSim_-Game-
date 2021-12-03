from enemy import Enemy
from room import Room
import random
import sys

class Walls(Room):
	raiders = ["Raider Beserker", "Raider Grunt", "Raider Gunner", "Raider", "Raider Merc", "Raider Bruiser"]

	def __init__(self, name):
    		'''
			constructor to create the walls object
			'''
		super().__init__(name)
		self.description = """\n
		You stand at the walls protecting your base.
		You see that the south wall has been damaged and will need to be repaired.
		The main gate is offline and unlocked.
		The turrets are offline and damaged. 
		You can head north to the courtyard. 
		\n"""
		self.contents = []
		self.doors = {"n": "courtyard"}
		self.special = ["Damaged Walls"]
		self.enemy = []

	def get_random_enemy(self):
		return None

	def spawn(self):
		for raider in Walls.raiders:
			self.enemy.append(Enemy(raider, random.randint(5, 10), random.randint(5, 10)))
		self.enemy.append(Enemy("Raider Leader", random.randint(10, 15), random.randint(10, 15) ))
		print("The raiders have returned!")


	def show_enemy(self):
		for i in self.enemy:
			print("In the group of raiders, there is a {} with {} HP and {} attack points!".format(i.name, i.health, i.attack_pts))