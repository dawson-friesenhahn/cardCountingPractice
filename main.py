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
        self.otherPlayerHands= [ [] for i in range(otherPlayers)]
        self.playerHand= Hand()
        self.dealerHand= Hand()

        self.deck= Deck(numDecks)
        
        self.root= root
        
        self.player_frame= ttk.Frame(self.root, width=100, height=100, padding=10)
        self.player_frame.grid(row=1, column=0)
        self.showPlayerTotal= True
        self.playerTotalLabel= ttk.Button(root, text="Player Total: ", command= self.togglePlayerHandTotalLabel)
        self.playerTotalLabel.grid(row=1, column=2)

        self.dealer_frame= ttk.Frame(self.root, width= 100, height= 100, padding= 10)
        self.dealer_frame.grid(row=0, column=0)
        self.dealerDownCardTk= None
        self.dealerDownCard= None

        self.hitButton= ttk.Button(root, text="Hit", command=self.hit)
        self.hitButton["state"] = "disabled"
        self.hitButton.grid(column=0, row=2)
        self.standButton= ttk.Button(root, text="Stand", command=self.stand)
        self.standButton.grid(column=1, row=2)
        self.dealButton= ttk.Button(root, text= "Deal", command=self.deal)
        self.dealButton.grid(column=2, row= 2) 

        self.photo_images= []

    def togglePlayerHandTotalLabel(self):
        self.showPlayerTotal = not self.showPlayerTotal
        self.updateHandTotalLabel(self.playerTotalLabel, self.playerHand)

    def updateHandTotalLabel(self, label, hand):
        if self.showPlayerTotal:
            self.playerTotalLabel.config(text= f"Player Total: {hand.calculateTotal()}")
        else:
            self.playerTotalLabel.config(text= "Show player hand total")

    def addCardToTk(self, frame, card):
        tkImage= self.getTkImageForCard(card, frame)
        tkCard = ttk.Label(frame, image=tkImage)
        tkCard.pack(side="left")
        # Keep a reference to the PhotoImage object
        self.photo_images.append(tkImage)
        self.root.update()
        return tkCard

    def deal(self):
        self.photo_images.clear()
        self.dealerHand.clear()
        self.playerHand.clear()
        
        
        #deal two to main player first
        for i in range(2):
            newCard= self.deck.draw()
            self.playerHand.append(newCard)
            self.addCardToTk(self.player_frame, newCard)     
            self.updateHandTotalLabel(self.playerTotalLabel, self.playerHand)    
        


        #deal two each extra player
        
        #deal one face down to dealer
        self.dealerDownCard= self.deck.draw()
        self.dealerDownCard.show_back= True
        self.dealerHand.append(self.dealerDownCard)
        self.dealerDownCardTk= self.addCardToTk(self.dealer_frame, self.dealerDownCard)

        #deal one face up to dealer
        newCard= self.deck.draw()
        self.dealerHand.append(newCard)
        self.addCardToTk(self.dealer_frame, newCard)

        self.hitButton['state']= "enabled"
        self.standButton['state'] = 'enabled'

    def hit(self):
        newCard= self.deck.draw()
        self.playerHand.append(newCard)
        self.addCardToTk(self.player_frame, newCard)
        self.updateHandTotalLabel(self.playerTotalLabel, self.playerHand) 

    def getTkImageForCard(self, card, frame):
        imgName= "./Images/" + card.getFullName() + ".png"
        print(imgName)
        img= Image.open(imgName)

        # Resize the image to fit the size of the parent frame
        parent_width = frame.winfo_width()
        parent_height = frame.winfo_height()

        print(f"Parent width, height: {parent_width}, {parent_height}")
        aspect_ratio = img.width / img.height
        if parent_width / aspect_ratio < parent_height:
            new_width = int(parent_width)
            new_height = int(new_width / aspect_ratio)
        else:
            new_height = int(parent_height)
            new_width = int(new_height * aspect_ratio)

        print(f"w: {new_width}, h:{new_height}")
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        return ImageTk.PhotoImage(img)

    def stand(self):
        self.dealerDownCard.show_back= False
        tkImage= self.getTkImageForCard(self.dealerDownCard, self.dealer_frame)
        self.dealerDownCardTk.config(image=tkImage)
        self.photo_images.append(tkImage)
        self.hitButton['state']= "disabled"
        self.standButton['state']= 'disabled'



def main():
    root = tk.Tk()
    root.title("BlackJack!")
    bj= Blackjack(root)
    frm= ttk.Frame(root, padding=10)
    frm.grid()
    
    root.mainloop()
    

if __name__ == "__main__":
    main()