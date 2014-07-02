#gofish.py
import random

class Card(object):
    """ represents a standard plating card"""

    rank_str = (None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a")
    suit_str = ("c", "d", "h", "s")

    def __init__(self, rank = 1, suit = 0):
        # creates cards
        self._suit = suit
        self._rank = rank

    def __str__(self):
        """ Returns readable string representation"""
        return "%s%s" % (Card.rank_str[self._rank], Card.suit_str[self._suit])

    def __cmp__(self, other):
        # compares this card to other
        # if this > other: returns positive number
        # if other > this: returns negative number
        # if equivalent: returns 0
        return cmp(self._rank, other.rank)

class Deck(object):
    """ Represents a deck of cars (list of Card objects) """

    def __init__(self, card):
        # creates deck
        self._card = card
        self._deck = []
    
    def get_deck(self):
        return self._deck

    deck = property(get_deck)

    @staticmethod 
    def make_basic_deck(self, card, num_decks = 1):
        # creates basic a basic deck with certain number of decks
        for i in range(num_decks):
            for suit in range(4):
                for rank in range(13):
                    card_str = card.rank_str[rank] + card.suit_str[suit]
                    self._deck.append(card_str)
                    return self._deck

    def shuffle(self):
        # randomizes all 52 cards in deck
        shuffled_deck = random.shuffle(Deck.make_basic_deck(card, num_decks))
        #shuffled_deck = random.shuffle(self.deck)
        return shuffled_deck

class Dealer(object):
    def __init__(self):
        # creates dealer
        self._dealer = dealer
        self._dealerdeck = []
    
    def get_dealerdeck(self):
        return self._dealerdeck

    dealerdeck = property(get_dealerdeck)
    
    def deal_(self, num_players = 2, num = 1):
        # deals number of cards (num) out to each player (one at a time)
        # returns list of dealt cards
        dealerdeck = deck.shuffle()
        player_hand = [dealerdeck[num::num_players] for num in range(0, num_players)] ###
        return player_hand

    def get_playerhand(self):
        return player_hand

    player_hand = property(get_playerhand)
    
    def remove_card(self):
        # removes card/s from deck list via calling deal()
        for i in deal(num_players, num):
            print dealerdeck.pop([i])

class Hand(object):
    def __init__(self, dealer):
        # creates hand via getting cards from dealer
        self._hand = dealer.player_hand ####

    def get_hand(self):
        return self._hand

    hand = property(get_hand)

    def draw(self, dealer):
        # gets card from dealerdeck for starting hand or for "go fish"
        # adds card to hand (list)
        while not self.check_match(card_rank):
            hand.append([dealer.dealerdeck[i]])
        return self.get_hand()

    def check_match(self, card_rank): # special class- gofish
        # compares hand with requested card
        # if match: return true
        i = 0
        while i < len(hand):
            if hand[i][0] == card_rank:
                return True 

    def remove_match(self):
        # if check_match is true: remove card from hand
        for i in hand:
            if self.check_match(card_rank):
                hand.pop([i])
        return self.get_hand()

    def count_book(self):
        # counts number of "books"
        # if complete_suit is true: increment counter 
        # return total number of "books"
        i = 0
        for 
        
        return total_books

    def complete_suit(self):
        # counts the number of cards in a suit
        # if 4 of a kind: return true
        # else: return false
        i = 0
        while i < 4:
            if hand[i][0] == hand[i + 1][]

        pass