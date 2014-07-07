#basegofish.py
import random

rank_str = [None,'ACE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING']

suit_str = ['SPADES','CLUBS','HEARTS','DIAMONDS']

class Card(object):
    """ represents a standard plating card"""

    def __init__(self, rank = 0, suit = 1):
        # creates card object
        self._rank = rank
        self._suit = suit

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
        for i in range(num_decks):
            for suit_str in range(4):
                for rank_str in range(1, 14):
                    deck.insert_card(Card(rank_str, suit_str))
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
        while ran_cardrank == None:
            ran_cardrank = random.choice(rank_str)
        return ran_cardrank

    def insert_card(self, card):
        self._deck.append(card)

class Table(object):
    # Table keeps track of players, their moves, announces them, and....
    # tupled list of players
    def __init__(self, players, num_players = 2):
        self._players = players
        for i in range(len(num_players)):
            self._players.append()
        all_players = tuple(self._players)

    def get_all_players(self):
        return all_players

def play_go_fish(table):
    # creates Go Fish game and has all the logic
    deck = Deck.make_basic_deck()
    deck.shuffle()
    # deals players hand of cards
    for i in range(5):
        for player in players:
            player.add_cards_to_hand(deck.draw())
            get_go_fish_hand(player)
            player.seat_at_table()

    # start to play the game
    i = 0
    while True:
        while opponent_player == player[i]:
            opponent_player = random.choice(Table.get_all_players())
            
        ran_cardrank = deck.gen_ran_cardrank()
        card = Card(ran_cardrank, None)

        while search_hand(opponent_player, card):
            tmp = opponent_player.remove_cards_from_hand(card)
            player[i].add_cards_to_hand(tmp)
            if tmp is None:
                print "Go Fish, %s take card from deck" % player[i]
                player[i].add_cards_to_hand(deck.draw())
        i = (i + 1) % len(players)

        if deck.check_deck_size == 0:
            print "Game over!"
            # winner is the player with the most books
            player_finish_rank(Table.get_all_players())
            

def get_go_fish_hand(player):
    # converts players hand to cards with no suits, just rank
    go_fish_hand = player.get_hand()
    for n in go_fish_hand:
        go_fish_hand[n][n] = [n][0]
        return go_fish_hand

def search_hand(player, card):
    # searches opponent's hand for card rank
    # if cards in player hand: return True
    pass 

def remove_cards_from_hand(cards):
    # removes cards from player's hand
    # if search_hand True: remove cards and return list
    # else: return None
    pass

def add_cards_to_hand(cards):
    # gets list of cards from function get_cards_from_player and appends card to hand
    pass

def player_finish_rank(players):
    # scans through all player's hands to determine winner
    # player with most books is the winner
    best_player = None
    best_book_count = 0
    for player in players:
        if player.count_books() > best_book_count:
            best_player = player
            best_book_count = player.count_books()

    sorted_players = sorted(players, cmp=lambda x, y: x.count_books() > y.count_books())
    print "List of Finishing Places (Win to Lose): %s" % sorted_players

def no_cheating(table, deck):
    # scans through the deck and player's cards to make sure no one is lie and no one creates any new cards to cheat!
    for player in Table.get_all_players():
        if card in deck and player:
            idx += 1
            if idx > (len(deck)/52):
                print "Cheater %s" % player
                player.remove_cards_from_hand(card)

class Player(Deck):
    """ class of players, stores players name and hand"""

    def __init__(self, name = " "):
        # creates player object
        self.name = name
        self.hand = []

    def get_hand(self):
        #returns players hand
        return self.hand

    def seat_at_table(self):
        # places player at Table object
        pass

    def __str__(self):
        """ String representation of player object"""
        return self.name

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