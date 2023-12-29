
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
    

