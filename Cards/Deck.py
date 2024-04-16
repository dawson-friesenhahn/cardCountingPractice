from Card import Card
from Card import Suit
import random
class Deck:
    def __init__(self, num_decks=1):
        self.cards= []
        for decks in range(num_decks):
            for suit in range(4):
                for num in range(1, 14):
                    self.cards.append(Card(Suit(suit), num))
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    def getRemainingCards(self):
        return len(self.cards)
    

if __name__ == "__main__":
    x= Deck(2)
    for i in range(55):
        card= x.draw()
        print(card.getFullName())
        print(f"{x.getRemainingCards()} cards left")