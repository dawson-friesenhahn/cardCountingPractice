from enum import Enum

class Suit(Enum):
    HEARTS= 0
    SPADES= 1
    DIAMONDS= 2
    CLUBS= 3

CARD_NUM_TO_CARD_NAME = {1: "ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "jack", 12: "queen", 13: "king"}


class Card:
    def __init__(self, suit, num):
        self.suit= suit
        self.num= num

    def getFullName(self):
        return CARD_NUM_TO_CARD_NAME[self.num] + "_of_" + str(self.suit.name).lower()
        

    
if __name__ == "__main__":
    x= Card(Suit.HEARTS, 12)
    print(x.getFullName())
    print(Suit.keys())