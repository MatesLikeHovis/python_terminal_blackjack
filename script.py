
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


cardList = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
valueList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
suitList = ["Spades", "Diamonds", "Hearts", "Clubs"]
cardCatalogue = []
for card in cardList:
    value = valueList[cardList.index(card)]
    for suit in suitList:
        thisCard = Card(card, suit, value)
        cardCatalogue.append(thisCard)
print(cardCatalogue)
