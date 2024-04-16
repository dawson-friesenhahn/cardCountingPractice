from .Card import Card, CARD_NUM_TO_CARD_NAME

class Hand:
    def __init__(self):
        self.cards= []

    def append(self, newCard):
        self.cards.append(newCard)

    def clear(self):
        self.cards.clear()

    def calculateTotal(self):
        total= 0
        num_aces= 0
        for card in self.cards:
            if CARD_NUM_TO_CARD_NAME[card.num] == "ace":
                num_aces +=1
            else:
                if card.num >= 10:
                    total +=10
                else:
                    total += card.num
        
        #at most, we can use one ace as an 11
        if total + (num_aces -1) <= 10:
            total = total + (num_aces -1) + 11
        else:
            total = total + num_aces

        return total
    
    def __str__(self):
        ret= ""
        if len(self.cards) == 0:
            return "Empty hand"
        else:
            ret= str(self.cards[0])
            for i in range(1, len(self.cards)):
                ret += ", " + str(self.cards[i])
        return ret


if __name__ == "__main__":
    from Cards import Deck
    from Cards.Card import Suit
    x = Deck.Deck()

    hand= Hand()
    hand.append(Card(Suit.CLUBS, 9))
    hand.append(Card(Suit.CLUBS, 1))
    hand.append(Card(Suit.CLUBS, 1))
    print(hand)
    print(hand.calculateTotal())
