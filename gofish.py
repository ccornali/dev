#gofish.py
import random

# rank and suit class
class Card(object):
    """ represents a standard plating card"""

    rank_str = (None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a")
    suit_str = (None, "c", "d", "h", "s")

    def __init__(self, rank = 1, suit = 1):
        # creates cards
        self._suit = suit
        self._rank = rank
        # raise valueerror and typeerror
    
    def __str__(self):
        """ Returns readable string representation"""
        return "%s%s" % (Card.rank_str[self._rank], Card.suit_str[self._suit])

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

class Deck(object):
    """ Represents a deck of cars (list of Card objects) """

    def __init__(self):
        # creates deck
        self._deck = []

    @staticmethod 
    def make_basic_deck(num_decks = 1):
        deck = Deck()
        # creates basic a basic deck with certain number of decks
        for i in range(num_decks):
            for suit in range(4):
                for rank in range(13):
                    deck.insert_card(Card(rank, suit))
        return deck

    def shuffle(self):
        # randomizes all cards in deck
        self._deck = random.shuffle(self._deck)

    def draw(self):
        return self._deck.pop()

    def insert_card(self, card):
        self._deck.append(card)

class Table(object):
    def __init__(self, players):
        self._players = players

    def announce(self, message):
        pass



def play_go_fish(table):
    # creates game with array of players and deals them cards
    deck = Deck.make_basic_deck()
    deck.shuffle()
    for i in range(5):
        for player in players:
            player.receive_card(deck.draw())

    for player in players:
        player.sit_at_table(table)

    i = 0
    while True:
        move = player[i].get_next_move()
        if move == 'hey j, do you have any aces?':
            cards = player[j].give_me('aces')
            if cards is None:
                player[j].receive_card(deck.draw())
        i = (i + 1) % len(players)




class Player(object):
""" class of players that play Go Fish"""


class Hand(object):
    """ contains subclass for game Go Fish! """

    def __init__(self):
        # creates hand via getting cards from dealer
        self._hand = Dealer.player_hand ####
        self.index = len(Dealer.player_hand)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self._hand

    def get_hand(self):
        return self._hand

    hand = property(get_hand)

    def draw(self, dealer):
        # gets card from dealerdeck for starting hand or for "go fish"
        # adds card to hand (list)
        while not self.check_match(card_rank):
            hand.append([dealer.dealerdeck[i]])
        return self.get_hand()

class GoFish(object):
    def __init__(self, card):
            # creates gofish hand
            card = Card(rank, None)
            self._gf_hand = Hand.__init__
            pass

    def check_match(self, card_rank): # special class- gofish
        # compares hand with requested card
        # if match: return true
        i = 0
        while i < len(hand):
            if hand[i][0] == card_rank:
                return True 

    def remove_match(self):
        # if check_match is true: remove card from hand
        for i in self._gf_hand:
            if Hand.check_match(card_rank):
                hand.pop([i])
        return self.get_hand()

    def count_book(self):
        # counts number of "books"
        # if complete_suit is true: increment counter 
        # return total number of "books"
        #for total_books in range(len(self._gf_hand)):
        #    if self.complete_suit():
        #        total_books += 1
        total_books = 0
        while self.complete_suit():
            total_books += 1
        return total_books

    def complete_suit(self):
        # counts the number of cards in a suit
        # if 4 of a kind: return true
        # else: return false
        i = 0
        while i < 4 and Hand.next():
            if hand[i] == hand[i + 1]:
                return True
            else:
                return False