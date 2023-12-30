import random

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
    return int(bet)

def shuffle_cards():
    cardDeck.extend(discardDeck)
    shuffleAmount = 150
    for i in range(shuffleAmount):
        cardPosition = random.randrange(0,50)
        cardDeck.insert(cardPosition, cardDeck.pop())

def draw_player_card(thisPlayer):
    newCard = cardDeck.pop()
    if newCard.name=="Ace" and thisPlayer.value <= 10:
        newCard.value = 11
    elif (newCard.name=="Ace"):
        newCard.value = 1
    thisPlayer.cardValue += newCard.value
    print(f"{thisPlayer.name} has drawn {newCard}")
    thisPlayer.cards.append(newCard)

def show_players_cards(thisPlayer):
    print(f"{thisPlayer.name} has these cards:")
    for card in thisPlayer.cards:
        print(f"{thisPlayer.card}")

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

def play_game():
    bet = get_wager()
    shuffle_cards()
    print("Drawing Cards")
    stayflag = False
    draw_player_card(player)
    draw_player_card(dealer)
    draw_player_card(player)
    draw_player_card(dealer)
    while not stayflag:
        show_players_cards(player)
        move = get_player_move
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

startingMoney = 1000
maximumBet = 100
minimumBet = 10


print("Welcome to Python Blackjack.")
print("Please input your name!: ")
playerName = input("")
player = Player(playerName, startingMoney, [], 0)
dealer = Player("The Dealer", startingMoney, [], 0)

play_game()


