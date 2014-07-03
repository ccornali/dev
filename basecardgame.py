#basecardgame.py
import random
from enum import Enum

class Suit(Enum):
    """Enum class for card suit"""

    SPADES = 1
    CLUBS = 2
    HEARTS = 3
    DIAMONDS = 4

    def __init__(self):
        # creates suit of card
        self._suit = suit
        if not isinstance(self._suit, basestring):
            raise TypeError
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
        if not isinstance(self._rank, basestring):
            raise TypeError
            print "Invalid input!"

    def __str__(self):
        return "%s" % self._rank
#rank_str = [None,'ACE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING']

#suit_str = [None,'SPADES','CLUBS','HEARTS','DIAMONDS']

#Suit = Enum('Suit', 'UNKNOWN SPADES CLUBS HEARTS DIAMONDS')
#Rank = Enum('Rank', 'ACE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING')

class Card(object):
    """ represents a standard plating card"""

    def __init__(self, rank = 1, suit = 1):
        # creates card object
        self._rank = Rank
        self._suit = Suit

    def __repr__(self):
        """ Returns readable string representation"""
        return "%s of %s" % (self._rank, self._suit)

    def __eq__(self, other):
        """Compares two cards for equality"""
        if not isinstance(other, Card):
            return False
        return self._rank == other.rank and self._suit == other.suit

    def __ne__(self, other):
        """Compares two cards for inequality"""
        return not self.__eq__(other)

class Deck(object):
    """ Represents a deck of cars (list of Card objects) """

    def __init__(self):
        # creates deck
        self._deck = []

    @staticmethod 
    def make_basic_deck(num_decks = 1):
        deck = Deck()
        # creates basic a basic deck with certain number of decks
        # [(s, r) for x in Suit for y in Rank]
            # deck.insert_card(Card(Rank, Suit))
        #for i in Suit:
            #for v in Rank:
        for i in range(num_decks):
            for suit in range(4):
                for rank in range(1, 14):
                    deck.insert_card(Card(Rank, Suit))
        return deck

    def shuffle(self):
        # randomizes all cards in deck
        self._deck = random.shuffle(self._deck)

    def draw(self, hands):
        # deals card from deck
        if self.check_deck_size():
            raise IndexError
            print "No More Cards in Deck"
        return self._deck.pop()

    def check_deck_size(self):
        # return length of deck or size of deck
        # if then statement to test of cards are left in deck
            if not self._deck:
                return False
            else:
                return True

    def gen_ran_cardrank(self):
        # generates random card rank
        ran_cardrank = random.choice(Rank)
        return ran_cardrank

    def insert_card(self, card):
        self._deck.append(card)

class Table(object):
    # Table keeps track of players, their moves, announces them, and....
    def __init__(self, players, num_players = 2):
        self._players = players
        for i in range(len(num_players)):
            self._players.append()
        all_players = list(enumerate(self._players))

    def get_all_players(self):
        return all_players

    def announce(self, message, player):
        # tells all players a message
        pass

def play_go_fish(table):
    # creates Go Fish game and had all the logic
    deck = Deck.make_basic_deck()
    deck.shuffle()
    # deals players hand of cards
    for i in range(5):
        for player in players:
            player.receive_card(deck.draw())
    
    # places players at table
    #for player in players:
    #    player.sit_at_table(table)
  
    # start to play the game
    i = 0
    while True:
        # if match found remove card from player[i] hand and give to player[j] hand
        opponent_player = random.choice(Table.get_all_players())
        while opponent_player == player[i]:
            opponent_player = random.choice(Table.get_all_players())
            
        ran_cardrank = deck.gen_ran_cardrank()
        cards = Card(ran_cardrank, 0)

        opponent_player_hand = opponent_player.get_player_hand()
        
        for cards in opponent_player_hand[:]:
            get_cards = opponent_player.remove_cards_from_hand(cards)
            player[i].receive_card(get_cards)
            if cards is None:
                print "Go Fish, %s take card from deck" % player[i] 
        i = (i + 1) % len(players)

        if deck.check_deck_size == 0:
            print "Game over!"
            # winner is the player with the most books

            best_player = None
            best_book_count = 0
            for player in players:
                if player.count_books() > best_book_count:
                    best_player = player
                    best_book_count = player.count_books()

            sorted_players = sorted(players, cmp=lambda x, y: x.count_books() > y.count_books())
            print "List of Finishing Places (Win to Lose): %s" % sorted_players

class Player(Deck):
    """ class of players that play Go Fish"""

    def __init__(self, name = " "):
        # creates player object
        self.name = name
        self.hand = []

    def __str__(self):
        """ String representation of player object"""
        return self.name

    def receive_card(self, card):
        # player receives card from deck or player
        self.hand.append(card)
        self.get_player_hand()

    def sort_hand(self):
        """ sorts players hand by value (2's to Aces)"""
        value = []
        j = 13
        idx = 1
        for i in range(len(self.hand)):
            while j != 0:
                if self.hand[j][0] == 1:
                    self.hand.append(self.hand[i])
                else:
                    self.hand[j][0] == j
                    self.hand.insert(i, self.hand[i])
                j -= 1
        
    def remove_cards_from_hand(self, cards):
        # removes card from hand
        self.get_player_hand()
        for i in range(len(self.hand)):
            if cards in self.hand:
                self.hand.pop(cards)

    def get_player_hand(self):
        for n in enumerate(self.hand):
            self.hand[n][n] = [n][0]
        return self.hand

    def count_books(self):
        # counts number of "books"
        # if complete_suit is true: increment counter 
        # return total number of "books"
        total_books = 0
        while self.complete_suit():
            total_books += 1
        return total_books

    def complete_suit(self):
        # counts the number of cards in a suit
        # if 4 of a kind: return true
        # else: return false
        i = 0
        while i < 4:
            if self.hand[i][0] == self.hand[i + 1][0]:
                return True
            else:
                return False
