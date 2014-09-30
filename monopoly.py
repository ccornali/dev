class Property(object):
	value={cost: $, mortgage: $}
	rent={suite: $, 1: $}
	build={1 house: $, 2 houses: $}

	house=property(get_house_count)

	rent=property(get_rent)
	
	mortgage=property(get_mortgage)

class Bank(object):
	acct_bal=property(get_bal)

	money_inventory=property(get_money_inventory)

	house_inventory=property(get_houses)

	hotel_inventory=property(get_hotels)

class Player(object):
	bank_bal=property(get_bal)

	## list of all Property() owned
	properties_owned=property(get_owned)

	## list of all Property() mortgaged 
	properties_mortgaged=property(get_mortgaged)

	## nested list of monopolies acquired
	## monopoly=[[property1, property2, property3], [prop1, prop2]]
	monopoly=property(get_monopoly)

	def build(self, num_houses=1, property_owned[i]):
		## adds num_houses to Property(), if is_FundsSufficient() True
		pass

	def validate_Construction(self, num_houses=1, prop=Property, ):
	## enures the the player does not build more than they're allowed
	## checks for monopoly and then the number of houses on each property
	## if the additional house/houses is illegal, return False
	## else player is allowed to build, returns True
	pass

def if_Buy(property=Property(), decision=sting(y/n)):
	## if answer==y and is_Owned(property) False, return True
	pass

def acquire_Property(player, property=Property()):
	## if is_FundsSufficient(player, payment_amt) and if_Buy(property, player) True,
	## player append property to properties_owned
	## else, property is not appended
	pass

def deduct_Cash(entity=Object, amt=int):
	## subtracts cash amt from Bank() acct_bal or Player() bank_bal
	## if paying another player rent, entity is paying player
	## returns amount to be subtracted
	pass

def add_Cash(entity=Object, amt=int):
	## adds cash amt to Bank() acct_bal or Player() bank_bal
	## if recieving rent from another player, entity is property owner
	## returns amt to be added
	pass

def remove_House(entity=Object, num=1):
	## removes num houses from Bank() inventory or Player() property inventory
	pass

def add_House(entity=Object, num=1):
	## add house to Player() property invetory or Bank() inventory
	pass

def check_NumHouse(property):
	## returns the number of house on a property
	pass

def is_FundsSufficient(player=Player, payment_amt=int):
	## payment_amt=rent, property cost or house cost
	## checks to make sure Player has enough money for rent, property purchase or to buy houses/hotels
	## if sufficient, return True
	pass

def mortgage_Property(player=Player(), properties_owned[i]):
	## removes property from properties_owned and appends property to properties_mortgaged
	## deduct_Cash from Bank() acct_bal
	## add_Cash to Player() bank_bal
	pass

def is_Monopoly(player=Player):
	## checks if player has monopoly
	## if monopoly, return True
	pass

def dice_Roll():
	## randomly generated number of spaces for player to move based off two 'dice'
	## returns tuple (diceroll_1, diceroll_2)
	pass

def is_Doubles(dice_rollTuple):
	## if both numbers in dice_rollTuple are the same, return True
	pass

def is_owned(property):
	## checks to see if property is owned,
	## if properties{Property(): True}, property owned and cannot be purchased
	## if owned, return True
	pass

def auction_property(property):
	## if_Buy(property, decision) False, any player can bid
	pass

def get_OutofJail():
	pass

def if_broke(player):
	## before each turn, checks to see if player bank_bal >0
	## if bank_bal=0, return True
	pass

def remove_player(player):
	## if_broke(player) True, pop player from Board.player
	pass

'''
def pay_Rentto(player_paying, rent_amt):
	## amt deducted from player_paying
	## returns
	pass

def buy_building_back(self, num_houses=1):
	## if player sells building, gets building value back in cash 
	## if bank re-aquires building, 
	pass
'''

class Board(object):
	def __init__(self, num_players=2):
		## Board is a dictionary of Property() (properties={Property(): False}, not owned)
		## and a list of Players with one Bank
		bank=Bank()
		## for loop to create each player for num_players
		player=Player()
		pass

	properties_avail=property(get_avail_for_purchase)

	def pass_go(self, player=Object):
		## whenever Player passes go, Bank gives Player $200
		pass
	def is_SuperTax(self, player=Player()):
		## if player lands on space, True
		##     deduct_cash(player, amt=200) from player
		##     add_cash(bank, amt=200)
		## else, pass
		pass

	def is_IncomeTax(self, player=Player()):
		## if player lands on space, True
		##     deduct_cash(player, amt=10% * Player() bank_bal) from player
		##     add_cash(bank, amt= deduct_cash(player, amt=10% * Player() bank_bal))
		## else, pass
		pass

	def go_toJail(self, player):
		## 
		pass

	def if_monopoly_double_rent(owner=Player(), renter=Player()):
		## if is_Monopoly(player()) True,
		## add_Cash(owner, amt*2)
		##deduct_Cash(renter, amt*2)
		pass

	def get_winner(self):
		## checks to see which players are broke
		## loop with if_broke() True, count_broke+=1
		## if count_broke==num_players-1
		## end game
		pass

