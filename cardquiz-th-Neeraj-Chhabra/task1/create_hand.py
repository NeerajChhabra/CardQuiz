import deck_create
import card_create
class Hand(deck_create.Createdeck):
    """defines the hand of cards help  by a player"""
    
    def __init__(self, label=''):
        self.deckcards = []
        self.label = label


def find_defining_class(obj, method_name):
    """Finds and returns the class object that will provide 
    the definition of method_name (as a string) if it is
    invoked on obj.

    obj: any python object
    method_name: string method name
    """
    for ty in type(obj).mro():
        if method_name in ty.__dict__:
            return ty
    return None


if __name__ == '__main__':
    deck = deck_create.Createdeck()
    deck.shuffle()

    hand = Hand()
    number_of_cards=int(input("enter the number of cards you want to draw = "))
    deck.move_cards(hand, number_of_cards)
    print(hand)
