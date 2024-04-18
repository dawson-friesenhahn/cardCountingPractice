import tkinter as tk
from tkinter import ttk
from Cards.Deck import Deck
from Cards.Hand import Hand
from PIL import Image, ImageTk
from time import sleep

class Blackjack:
    def __init__(self, root, otherPlayers= 0, numDecks= 1):
        self.otherPlayers= otherPlayers
        self.numDecks= numDecks
        self.otherPlayerHands= [ Hand(root) for i in range(otherPlayers)]
        self.playerHand= Hand(root)
        self.dealerHand= Hand(root)

        self.deck= Deck(numDecks)
        
        self.root= root       

        self.player_frame= self.playerHand.mainFrame
        self.player_frame.place(relx=0, rely=0.6, relwidth=0.8, relheight=0.3)
        

        self.dealer_frame= self.dealerHand.mainFrame
        self.dealer_frame.place(relx=0, rely=0, relwidth=0.8, relheight=0.3)

        self.countsVisible= False
        self.countButton= tk.Button(root, text= "Show Counts", command= self.show_counts)
        self.countButton.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.2)


        self.hitButton= ttk.Button(root, text="Hit", command=self.hit)
        self.hitButton["state"] = "disabled"
        self.hitButton.place(relx=0, rely=0.9, relwidth=0.1, relheight=0.1)
        self.standButton= ttk.Button(root, text="Stand", command=self.stand)
        self.standButton.place(relx=0.1, rely=0.9, relwidth=0.1, relheight=0.1)
        self.dealButton= ttk.Button(root, text= "Deal", command=self.deal)
        self.dealButton.place(relx=0.2, rely=0.9, relwidth=0.1, relheight=0.1) 
        self.shuffleButton= tk.Button(root, text="Shuffle", command=self.shuffle)
        self.shuffleButton.place(relx=0.3, rely=0.9, relwidth=0.1, relheight=0.1)

        self.photo_images= []

    def shuffle(self):
        self.playerHand.clear()
        self.dealerHand.clear()
        self.deck.initialize_new_cards()
        self.updateCountsLabel()

    def updateCountsLabel(self):
        if self.countsVisible:
            runningCount= self.deck.running_count
            for card in self.dealerHand.cards:
                if card.show_back:
                    runningCount -= card.getHighLow()
            
            trueCount= runningCount / self.deck.getRemainingDecks()

            self.countButton.config(text=f"Running Count: {runningCount}\nTrue Count: {trueCount}")
        else:
            self.countButton.config(text="Show Counts")

    def show_counts(self):
        self.countsVisible = not self.countsVisible
        self.updateCountsLabel()

    def deal(self):
        self.photo_images.clear()
        self.dealerHand.clear()
        self.playerHand.clear()
      
        
        #deal two to main player first
        for i in range(2):
            newCard= self.deck.draw()
            self.playerHand.append(newCard)      


        #deal two each extra player
        
        #deal one face down to dealer
        newCard= self.deck.draw()
        newCard.show_back= True
        self.dealerHand.append(newCard)

        #deal one face up to dealer
        newCard= self.deck.draw()
        self.dealerHand.append(newCard)


        if self.playerHand.calculateTotal() == 21:
            if self.dealerHand.calculateTotal() == 21:
                self.push()
            else:
                self.playerBlackjack()


        self.hitButton['state']= "enabled"
        self.standButton['state'] = 'enabled'
        self.updateCountsLabel()

    def hit(self):
        newCard= self.deck.draw()
        self.playerHand.append(newCard)

        if self.playerHand.calculateTotal() > 21:
            print("you bust lmao")
            self.houseWins()
        self.updateCountsLabel()

    def dealerHit(self):
        newCard= self.deck.draw()
        self.dealerHand.append(newCard)

    def playerWin(self):
        print("Player wins!")

    def playerBlackjack(self):
        print("Blackjack!")
    
    def houseWins(self):
        print("House wins")

    def push(self):
        print("push")

    def stand(self):
        self.dealerHand.makeFirstCardFaceUp()
        self.hitButton['state']= "disabled"
        self.standButton['state']= 'disabled'

        while self.dealerHand.calculateTotal() < 17:
            self.dealerHit()
        
        playerTotal= self.playerHand.calculateTotal()
        dealerTotal= self.dealerHand.calculateTotal()

        if (dealerTotal >21):
            print("dealer Bust!")
            self.playerWin()
        elif playerTotal > dealerTotal:
            print("higher total!")
            self.playerWin()
        elif playerTotal < dealerTotal:
            self.houseWins()
        elif playerTotal == dealerTotal:
            self.push()

        self.updateCountsLabel()



def main():
    root = tk.Tk()
    root.title("BlackJack!")
    main_frame = tk.Frame(root, width=500, height=500, bg='green')
    main_frame.pack(fill=tk.BOTH, expand=True)
    bj= Blackjack(main_frame)
    
    
    root.mainloop()
    

if __name__ == "__main__":
    main()