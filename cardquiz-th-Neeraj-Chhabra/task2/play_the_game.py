import card_create
import create_hand
import deck_create

class Playgame(create_hand.Hand):
	""" lets play the game
	"""
	if __name__ == '__main__':	
		hand=create_hand.Hand()
		create_hand.draw_card_on_request(hand)



