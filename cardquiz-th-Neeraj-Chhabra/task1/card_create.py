class Createcard:
	""" 
   		This class creates a normal card
  
 	Attributes:
   		suit_by_number: [0,1,2,3]
   		rank_by_number: [1,2,3,4,5,6,7,8,9,10,11,12,13]
	"""
	
	suit_by_name = ["Clubs","Diamonds","Hearts","Spades"]
        rank_by_name = ["None","Ace","1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
	def __init__(self, suit_by_number=3, rank_by_number=13):
        	self.suit_by_number = suit_by_number
        	self.rank_by_number = rank_by_number

        def __str__(self):
    	       	"""Returns a human-readable string representation and returns strings."""
       		return '%s of %s' % (Createcard.rank_by_name[self.rank_by_number],Createcard.suit_by_name[self.suit_by_number])

