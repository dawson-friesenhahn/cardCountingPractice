from .Card import Card
from .Card import Suit
import random
class Deck:
    def __init__(self, num_decks=1, shuffleThreshold= 0.1):
        self.cards= []
        self.shuffleThreshold = shuffleThreshold
        self.num_decks= num_decks
        self.running_count= 0
        self.initialize_new_cards()

    def initialize_new_cards(self):
        for decks in range(self.num_decks):
            for suit in range(4):
                for num in range(1, 14):
                    self.cards.append(Card(Suit(suit), num))
        self.running_count= 0
        self.shuffle()
        
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        try:
            new_card= self.cards.pop()
        except:
            print("Deck was empty! shuffling...")
            self.initialize_new_cards()
            new_card= self.cards.pop()
        self.running_count += new_card.getHighLow()
        print(f"Running Count: {self.running_count}")
        return new_card
    
    def getRemainingCards(self):
        return len(self.cards)
    
    def getRemainingDecks(self):
        return self.getRemainingCards() / (self.num_decks * 52)
    

if __name__ == "__main__":
    x= Deck(2)
    for i in range(55):
        card= x.draw()
        print(card.getFullName())
        print(f"{x.getRemainingCards()} cards left")