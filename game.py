from player import Player
from armory import Armory
from kitchen import Kitchen
from entry import EntryWay
from dining_room import DiningRoom
from courtyard import Courtyard
from walls import Walls
from bedroom import Barracks
from room import Room
from character import Character
from living_room import LivingRoom
from enemy import Enemy
from reactor import Reactor
from workshop import Workshop
import random
import time

class Game:
	def __init__(self):
		self.intro = """Welcome to the old city!
You are the sole survivor of an old city  built into a mountain. Raiders attacked your fledgling homestead and killed the other city , your friends and family.
After burying the dead, you survey the colony. The only way into the city is through the south wall and its crumbling in portions. 
You see that the main power to the base is offline, leaving the autoturrets offline and the main gate unlocked. 
You'll have to search your base for whatever supplies are left. The colony was running low on supplies before the raider attack. The attack has left the base mostly barren. 
You might find some items leftover, however. You'll need to find ammo, weapons and building supplies to fix the south walls.  
Each room will tell you which directions you can go. Be careful because you heard some crashes and rustling in the colony as you buried the bodies. 
Complete the game by defeating the raiders and repairing your base. You can move north, south, east or west by typing n,s,e or w. 
Type q to end the program.\n"""

	def show_intro(self):
		print("\nHello, {}. {} ".format(player.name, self.intro))

	def main(self):
		self.show_intro()
		run = True
		while run:
			new_loc = player.explore(player.location)
			if new_loc == "armory":
				loc = armory
			elif new_loc == "kitchen":
				loc = kitchen
			elif new_loc == "entry":
				loc = entry
			elif new_loc == "dining":
				loc = dining
			elif new_loc == "walls":
				loc = walls
			elif new_loc == "barracks":
				loc = barracks
			elif new_loc == "courtyard":
				loc = courtyard
			elif new_loc == "lr":
				loc = lr
			elif new_loc == "reactor":
				loc = reactor
			elif new_loc == "workshop":
				loc = workshop
			elif new_loc == "q":
				print("Exit game")
				run = False
				break
			else:
				print(new_loc)
				loc = player.location
			player.location = loc

game = Game()
armory = Armory("armory")
kitchen = Kitchen("kitchen")
entry = EntryWay("entry way")
walls = Walls("walls")
lr = LivingRoom("living room")
barracks = Barracks("barracks")
courtyard = Courtyard("courtyard")
dining = DiningRoom("dining room")
reactor = Reactor("reactor")
workshop = Workshop("workshop")
name = input("Enter name:  \n")
player = Player(name, 25, 10, courtyard)
game.main()