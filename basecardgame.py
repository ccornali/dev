#basecardgame.py
import random

def convert_player_input(p_input):
    p_input.lower()

    if p_input == 'j' or p_input == 'jack'
        p_input = 'J'
    if p_input == 'q' or p_input == 'queen'
        p_input = 'Q'
    if p_input == 'k' or p_input == 'king'
        p_input = 'K'
    if p_input == 'a' or p_input == 'aces'
        p_input = 'A'

    if p_input == 'c' or p_input == 'clubs'
        p_input = 'CLUBS'
    if p_input == 'd' or p_input == 'diamonds'
        p_input = 'DIAMONDS'
    if p_input == 'h' or p_input == 'hearts'
        p_input = 'HEARTS' 
    if p_input == 's' or p_input == 'spades'
        p_input = 'SPADES'
    return p_input

rank_str = (None,'ACE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING')

suit_str = (None,'SPADES','CLUBS','HEARTS','DIAMONDS')
    
Suit = Enum('Suit', 'SPADES CLUBS HEARTS DIAMONDS')
Rank = Enum('Rank', 'ACE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN JACK QUEEN KING')

class Card(object):
    """ represents a standard plating card"""

    def __init__(self, rank = 1, suit = 0):
        # creates card object
        self._rank = rank
        self._suit = suit

    def __repr__(self):
        """ Returns readable string representation"""
        return "%s of %s" % (self._rank, self._suit)

    def __eq__(self, other):
        """Compares two cards for equality"""
        if not isinstance(other, Card)
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
        for i in range(num_decks):
            for suit in range(4):
                for rank in range(1, 14):
                    deck.insert_card(Card(rank, suit))
        return deck

    def shuffle(self):
        # randomizes all cards in deck
        self._deck = random.shuffle(self._deck)

    def draw(self, hands):
        # deals card from deck
        if self.check_deck_size() == 0:
            raise IndexError: print "No More Cards in Deck"
        return self._deck.pop()

    def check_deck_size(self):
        # return length of deck or size of deck
        # if then statement to test of cards are left in deck
            if not self._deck:
                deck_len = 0
            else:
                deck_len = len(self._deck)
            return deck_len

    def insert_card(self, card):
        self._deck.append(card)

class Table(object):
    # Table keeps track of players, their moves, announces them, and....
    def __init__(self, players):
        self._players = players
        for i in enumerate(self._players):
            self.

    def announce(self, message, player):
        # tells all players a message
        
        pass

    def play_again(self):
        if 

def play_go_fish(table):
    # creates Go Fish game and had all the logic
    deck = Deck.make_basic_deck()
    deck.shuffle()
    # deals players hand of cards
    for i in range(5):
        for player in players:
            player.receive_card(deck.draw())
    
    # places players at table
    for player in players:
        player.sit_at_table(table)

    # chooses random player to start 
    players_order 
  
    # start to play the game
    
    for play_order in range(len(players_order)):
        i = 0
        while True:
        # if match found remove card from player[i] hand and give to player[j] hand
            move = player[i].get_next_move(Card(rank,suit), player[j])

            if move == "hey %s, do you have any %s?", (player[j], card) :
                cards = player[j].give_card_to_player(Card(rank, suit))
                if cards is None:
                    player[i].receive_card(deck.draw())
                    print "Go Fish, %s take card from deck" % player[i]
                else:
                    player[i].recieve_card(cards)
            i = (i + 1) % len(players)

        if deck.check_deck_size == 0:
            print "Game over!"
            winners = 0
            for p in players:
                if player[p].count_books > player[p + 1].count_books:
                    print "Player %s wins!" % player[i]
                    break
                else:
                    player[p].count_books == player[p + 1].count_books:
                    winners += 1
                    if winners == 2:
                        print "Tie! Players %s and %s wins!" % (player[p], player[p + 1])
                    if winners > 2:
                        print "More than two players tied, cannot determine winner"
                play_again = new_input("Do you wish to play again?(y or n) ")
                count = 0
                if player[p].response(play_again) == 'y':
                        count += 1


class Player(Deck):
""" class of players that play Go Fish"""

    def __init__(self, name = " "):
        # creates player object
        self.name = name
        self.hand = []

    def __str__(self):
        """ String representation of player object"""
        return self.name

    def response(self, pinput):
        return pinput

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
                    self.hand[j][0] == j:
                    self.hand.insert(i, self.hand[i])
                j -= 1

    def receive_card(self, card):
        # player receives card from deck or player
        self.hand.append(card)
        pass

    def sit_at_table(self): ## rename, prep
        # places player at table object
        pass

    def get_next_move(self, card, other_player):
        # players next move, asks for card
        return "hey %s, do you have any %s?", (other_player, card)

    def give_card_to_player(self, cards):
        # give requested card to player[i]
        if card in self.hand:
            self.hand.pop(card)

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
