# Deal 'Em
# Dan Soloha
# 9/12/2019

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print(f"{self.value} of {self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Clubs", "Hearts", "Spades", "Diamonds"]:
            for v in range(1, 14):
                if v == 1:
                    v = "A"
                elif v == 11:
                    v = "J"
                elif v == 12:
                    v = "Q"
                elif v == 13:
                    v = "K"

                self.cards.append(Card(s, v))
            
    def show(self):
        for c in self.cards:
            c.show()

num_players = int(input("How many players are there? "))
num_cards = int(input("How many cards in each hand? "))