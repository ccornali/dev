#blackjack.py

class Dealer(object):
    def __init__(self):
        # creates dealer
        pass

    def deal_cards(self, num):
        # deals number of card out to each player (one at a time)
        # returns list of dealt cards
        pass

    def remove_card(self, cards):
        # removes card/s from deck list via calling deal_cards
        pass

class Deck(object):
	def __init__(self):
        # creates deck
        pass

class Hand(object):
	def __init__(self, deck):
        # creates hand via getting cards from deck
        pass

    def hit(self, deck):
        # gets card from deck for starting hand or for "go fish"
        # adds card to hand (list)
        pass

    def check_blackjack(self):
    	# check if hand is over, under, or 21
    	# returns 
    	pass

class Player(object):
    def __init__(self):
        pass

    def hit(self): 
