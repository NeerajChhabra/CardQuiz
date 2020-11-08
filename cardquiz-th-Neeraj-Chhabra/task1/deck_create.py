import card_create
import random
class Createdeck:
    """creates a deck of cards and operations.

    Attributes:
      deckcards: []
    """
    
    def __init__(self):
        """creates a deck of 52 cards
        """
        self.deckcards = []
        for suit_by_number in range(4):
            for rank_by_number in range(1, 14):
                card = card_create.Createcard(suit_by_number, rank_by_number)
                self.deckcards.append(card)

    def __str__(self):
        """Represents the human readable cards.
        """
        res = []
        for card in self.deckcards:
            res.append(str(card))
        return '\n'.join(res)

    def add_card(self, card):
        """used to add a card to the deck.

        card: Createcard
        """
        self.deckcards.append(card)

    def remove_card(self, card):
        """removes a card from the deck and handles an exception.
        
        card: Createcard
        """
        try:
        	self.deckcards.remove(card)
	except:
		if len(self.deckcards)==0:
			print("card cannot be removed, deck is empty")
    def pop_card(self, i=-1):
        """remove and return the card, pops the top card in the deck by default.

        i
        """
	return self.deckcards.pop(i)

    def shuffle(self):
        """randomly shuffles the card"""
        random.shuffle(self.deckcards)

    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.
        """
        for i in range(num):
            hand.add_card(self.pop_card())


