import random

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return(f"{self.value} of {self.suit}")

class Deck:

	FULL_DECK = 52

	def __init__(self):
		suits = ("Hearts", "Diamonds", "Clubs", "Spades")
		values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
		self.cards = []
		[self.cards.append(Card(suit, value)) for suit in suits for value in values]

	def __repr__(self):
		return (f"Deck of {self.count()} cards")

	def count(self):
		return len(self.cards)

	def _deal(self, qty):
		if not self.count():
			raise ValueError('All cards have been dealt')
		return [self.cards.pop() for i in range(0,min(self.count(),qty))]
				
	def shuffle(self):
		if self.count() < Deck.FULL_DECK:
			raise ValueError ('Only full decks can be shuffled')
		random.shuffle(self.cards)
		return self

	def deal_card(self):
		return self._deal(1)[0]

	def deal_hand(self, hand_size):
		return self._deal(hand_size)

		