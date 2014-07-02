#cardgame.py
import random, itertools

def convert_player_input(p_input):
    p_input.lower()

    if p_input == 'j' or p_input == 'jack'
        p_input = 'j'
    if p_input == 'q' or p_input == 'queen'
        p_input = 'q'
    if p_input == 'k' or p_input == 'king'
        p_input = 'k'
    if p_input == 'a' or p_input == 'aces'
        p_input = 'a'

    if p_input == 'c' or p_input == 'clubs'
        p_input = 'c'
    if p_input == 'd' or p_input == 'diamonds'
        p_input = 'd'
    if p_input == 'h' or p_input == 'hearts'
        p_input = 'h' 
    if p_input == 's' or p_input == 'spades'
        p_input = 's'
    return p_input

class Suit(Enum):
    """Enum class for card suit"""

    SPADES = 1
    CLUBS = 2
    HEARTS = 3
    DIAMONDS = 4

    def __init__(self):
        # creates suit of card
        self._suit = suit
        convert_player_input(self._suit)
        if not isinstance(self._suit, basestring)
            raise TypeError:
                print "Invalid input!"

    def __str__(self):
        return "%s" % self._suit

class Rank(Enum):
    """Enum class for card rank """

    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

    def __init__(self):
        # creates rank of card
        self._rank = rank
        convert_player_input(self._rank)
        if not isinstance(self._rank, basestring)
            raise TypeError:
                print "Invalid input!"

    def __str__(self):
        return "%s" % self._rank

    def __iter__(self):
        return

class Card(object):
    """ represents a standard plating card"""

    rank_str = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "j", "q", "k", "a")
    suit_str = ("c", "d", "h", "s")

    def __init__(self, rank = 0, suit = 0):
        # creates cards
        self._suit = suit
        self._rank = rank

    def __str__(self):
       """ Returns readable string representation"""

        return "%s%s" % (Card.rank_str[self._rank], Card.suit_str[self._suit])

    def define_cards(self, rank, suit):
        self._cards = []
        for suit in range(4):
            for rank in range(13):
                card_str = rank_str[rank] + suit_str[suit]
                self._cards.append(card_str)
                return self._cards

    def __cmp__(self, other):
        # compares this card to other
        # if this > other: returns positive number
        # if other > this: returns negative number
        # if equivalent: returns 0
        c1 = self._suit, self._rank
        c2 = other.suit, other.rank
        return cmp(c1, c2)

class Deck(object):
    def __init__(self, card):
        # creates deck
        self._card = card
        self._deck = []

    @staticmethod 
    def make_basic_deck(self, num_decks = 1):
        # creates basic a basic deck with certain number of decks
        for i in range(num_decks):
            for suit in range(4):
                for rank in range(13):
                    #card_str = card.rank_str[rank] + card.suit_str[suit]
                    self._deck.append(self._card.__str__)
                    return self._deck

    def shuffle(self):
        # randomizes all 52 cards in deck
        self._deck = random.shuffle(Deck.make_basic_deck(num_decks))
        #shuffled_deck = random.shuffle(self.deck)
        return self._deck

    #def create_basic_deck(self, deck, num_decks):
    #    self._deck = list(itertools.product(range(1,14), ["Spade", "Heart", "Diamond", "Club"]))
    #    return self._deck

    def get_deck(self):
        return self._deck

    deck = property(get_deck)

class Dealer(object):
    def __init__(self, deck):
        # creates dealer
        self._dealer_deck = deck

    def deal_cards(self, deck, num):
        # deals number of card out to each player (one at a time)
        # returns list of dealt cards
        for i in range(num):
            deck[i][0], 
        pass

    def remove_card(self, cards):
        # removes card/s from deck list via calling deal_cards
        pass
class Hand(object):
    def __init__(self, deck):
        # creates hand via getting cards from deck
        pass

    def hit(self, deck):
        # gets card from deck for starting hand or for "go fish"
        # adds card to hand (list)
        pass

class Player(object):
    def __init__(self):
        # creates player
        pass

    def hit(self):
        # gets card from dealer
        pass