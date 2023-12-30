import random

# CLASSES
#
#

class Player:
    def __init__(self, name, money, cards, cardValue):
        self.name = name
        self.money = money
        self.cards = cards
        self.cardValue = cardValue

    def __repr__(self):
        return f"Player {self.name} has ${self.money}, holds the {self.cards} cards with a value of {self.cardValue}"
    
    def addMoney(self, amount):
        self.money += amount

    def RemoveMoney(self, amount):
        self.money -= amount

    def EmptyCards(self):
        self.cards = []
        self.cardValue = 0

class Card:
    def __init__(self, name, suit, value):
        self.name = name
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"A {self.name} of {self.suit}, worth {self.value}"

# GAMEPLAY FUNCTIONS
#
#

def get_wager():
    print(f"{player.name}, you currently have ${player.money}.")
    bet = input("Please type the amount you wish to bet:  ")
    try: 
        int(bet)
    except:
        print("You must input an integer amount as a bet.")
        return get_wager()
    if (int(bet) > maximumBet or int(bet) < minimumBet):
        print(f"You must wager between ${minimumBet} and ${maximumBet}.")
        return get_wager()
    if (int(bet) > player.money):
        print(f"You only have ${player.money} - you cannot bet above this amount.")
        return get_wager()
    if (int(bet) > dealer.money):
        print(f"The dealer only has ${dealer.money} - you cannot exceed this amount.")
        return get_wager()
    return int(bet)

def shuffle_cards():
    for card in discardDeck:
        cardDeck.append(discardDeck.pop())
    shuffleAmount = 150
    for i in range(shuffleAmount):
        cardPosition = random.randrange(0,50)
        cardDeck.insert(cardPosition, cardDeck.pop())

def draw_player_card(thisPlayer, showCardFlag = True):
    newCard = cardDeck.pop()
    if newCard.name=="Ace" and thisPlayer.cardValue <= 10:
        newCard.value = 11
    elif (newCard.name=="Ace"):
        newCard.value = 1
    thisPlayer.cardValue += newCard.value
    if showCardFlag:
        print(f"{thisPlayer.name} has drawn {newCard}")
    thisPlayer.cards.append(newCard)

def show_players_cards(thisPlayer):
    print(f"{thisPlayer.name} has these cards, worth {thisPlayer.cardValue}:")
    for card in thisPlayer.cards:
        print(f"{card}")

def get_player_move():
    print("Would you like to (S)tay or (H)it???  ")
    playerInput = input("")
    if playerInput == "S" or playerInput == "H":
        return playerInput
    else:
        print("Please type either S for Stay or H for Hit!!")
        return get_player_move()

def check_for_aces(thisPlayer):
    for card in thisPlayer.cards:
        if card.name=="Ace" and thisPlayer.value > 21 and card.value == 11:
            card.value = 1
            thisPlayer.cardValue -= 10

def return_cards_to_deck():
    for card in player.cards:
        discardDeck.append(player.cards.pop())
    for card in dealer.cards:
        discardDeck.append(dealer.cards.pop())
    player.cardValue = 0
    dealer.cardValue = 0

#THIS IS THE GAMEPLAY LOOP CALLED BELOW:
def play_game():
    bet = get_wager()
    shuffle_cards()
    print("Drawing Cards")
    stayflag = False
    draw_player_card(player)
    draw_player_card(dealer, False)
    draw_player_card(player)
    draw_player_card(dealer, False)
    while not stayflag:
        show_players_cards(player)
        move = get_player_move()
        if move == "S":
            stayflag = True
        else:
            draw_player_card(player)
            if player.cardValue > 21:
                check_for_aces(player)
                if player.cardValue > 21:
                    stayflag = True
    if player.cardValue > 21:
        print(f"Total card value is {player.cardValue} -- Player Busts!!!")
        return -1
    print(f"Player stands at {player.cardValue}.")
    dealerstay = False
    show_players_cards(dealer)
    while dealer.cardValue <= 16:
        print(f"Dealer holds {dealer.cardValue} and hits:")
        draw_player_card(dealer)
    if dealer.cardValue > 21:
        print("Dealer Busts!!! Player Wins")
        return bet
    elif dealer.cardValue > player.cardValue:
        print(f"Dealer's {dealer.cardValue} beats Player's {player.cardValue}")
        print("Dealer Wins.")
        bet *= -1
        print(f"Player Loses ${bet}")
        return bet
    elif dealer.cardValue == player.cardValue:
        print("Push!!!!")
        print("Player does not win or lose.")
        return 0
    else:
        print(f"Player's {player.cardValue} beats Dealer's {dealer.cardValue}")
        print("Player Wins.")
        print(f"Player Wins {bet}")
        return bet


cardList = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
valueList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
suitList = ["Spades", "Diamonds", "Hearts", "Clubs"]
cardDeck = []
discardDeck = []
for card in cardList:
    value = valueList[cardList.index(card)]
    for suit in suitList:
        thisCard = Card(card, suit, value)
        cardDeck.append(thisCard)


#Actual Gameplay begins here:
        
startingMoney = 1000
maximumBet = 100
minimumBet = 10
print("Welcome to Python Blackjack.")
print("Please input your name!: ")
playerName = input("")
player = Player(playerName, startingMoney, [], 0)
dealer = Player("The Dealer", startingMoney, [], 0)
while player.money > 0 and player.money < 2000:
    gameResult = play_game()
    player.money += gameResult
    dealer.money -= gameResult
    return_cards_to_deck()
if player.money <= 0:
    print(f"YOU ARE OUT OF MONEY")
    print("*********************")
    print("*****  YOU LOSE *****")
    print("*********************")
elif player.money >= 2000:
    
    print(f"YOU WON ALL THE MONEY")
    print("**********************")
    print("******  YOU WIN ******")
    print("**********************")

