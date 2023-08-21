from termcolor import colored
import random

colors = {"♣":"grey", "♦":"red", "♥":"red","♠":"grey"}
suits = ["♣", "♦", "♥","♠"]
ranks = ['A'] + list(range(2,10)) + ["X","J","Q","K"]
values = [11] + list(range(2,10)) + [10]*4

class Card:
	def __init__ (self,r,s):
		self.r = r
		self.s = s 
		self.v = values[ranks.index(r)]
		self.h = False

	def __str__ (self):
		if self.h:
			return "+-----+\n|#####|\n|#####|\n|#####|\n+-----+\n"
		else:
			return (f"+-----+\n|{colored(self.s,colors[self.s])}{self.r}   |\n|     |\n|   {self.r}{colored(self.s,colors[self.s])}|\n+-----+\n")

class Deck(list):
	def __init__ (self):
		super().__init__()

		for s in suits:
			for r in ranks:
				self.append(Card(r,s))

		random.shuffle(self)

	def __str__ (self):
		tmp = ""

		for j in range(0,len(self),7):
			for i in range(5):
				for c in self[j:j+7]:
					tmp += str(c).split("\n")[i]
				tmp += "\n"

		return tmp


class Hand(Deck):
	def __init__ (self):
		super().__init__()
		self.clear() # empty the list



class Game:
	def __init__(self):
		self.deck = Deck()
		self.house = Hand()
		self.player = Hand()
		# deal two cards for each player
		for i in range(2):
			self.house.append(self.deck.pop())
			self.player.append(self.deck.pop())

		self.house[0].h = True

		self.active = True
		self.play()

	def computeHand(self, hand):
		val = 0
		aces = 0

		for c in hand:
			val += c.v

			if c.r == 'A':
				aces += 1

		while val > 21 and aces > 0:
			val -= 10
			aces -= 1

		return str(val)


	def __str__(self):
		if self.active:
			tmp = "House (?)\n-------\n"
		else:
			tmp = "House (" + self.computeHand(self.house) +")\n-------\n"
		tmp += str(self.house)
		tmp += "\n\nPlayer (" + self.computeHand(self.player) + ")\n------\n"
		tmp += str(self.player)
		return tmp

	def play(self):
		while True:
			print (self)

			userChoice = input("1. Hit\n2. Stand\nPlease chose an option: ")

			if userChoice == "1":
				self.player.append(self.deck.pop())

				if int(self.computeHand(self.player)) > 21:

					self.active = False
					self.house[0].h = False
					print (self)
					print ("Game over. you lost :-(")
					return
			elif userChoice == "2":
				self.active = False
				self.house[0].h = False

				while int(self.computeHand(self.house)) < 17:
					self.house.append(self.deck.pop())
					print (self)

				if int(self.computeHand(self.house)) > 21:
					print ("You win !!!!")
				elif int(self.computeHand(self.house)) == int(self.computeHand(self.player)):
					print ("It's a daw")
				elif int(self.computeHand(self.house)) < int(self.computeHand(self.player)):
					print ("You win !!!")
				else:
					print ("Game over. you lost :-(")

				return


game = Game()






