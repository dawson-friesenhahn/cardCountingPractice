from enum import Enum

class Suit(Enum):
    HEARTS= 0
    SPADES= 1
    DIAMONDS= 2
    CLUBS= 3

CARD_NUM_TO_CARD_NAME = {1: "ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "10", 11: "jack", 12: "queen", 13: "king"}

def CARD_NUM_TO_CARD_HI_LOW(cardNum):
    if cardNum < 1 or cardNum > 13:
        raise ValueError("Invalid card number")
    if cardNum == 1 or cardNum > 9:
        return -1
    elif cardNum > 1 and cardNum < 7:
        return 1
    elif cardNum >= 7 and cardNum <= 9:
        return 0
    else:
        raise ValueError("Invalid Card Number")

class Card:
    def __init__(self, suit, num, show_back= False):
        self.suit= suit
        self.num= num
        self.show_back= show_back

    def getFullName(self):
        if self.show_back:
            return "back_of_card"
        else:
            return CARD_NUM_TO_CARD_NAME[self.num] + "_of_" + str(self.suit.name).lower()
    
    def getHighLow(self):
        return CARD_NUM_TO_CARD_HI_LOW(self.num)
    
    def __str__(self):
        return CARD_NUM_TO_CARD_NAME[self.num] + " of " + str(self.suit.name).lower()
        

    
if __name__ == "__main__":
    x= Card(Suit.HEARTS, 12)
    print(x.getFullName())