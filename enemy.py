from character import Character

class Enemy(Character):
	def __init__(self, name, health, attack_pts):
    		'''
			function to create enemy
			'''
		super().__init__(name, health, attack_pts)