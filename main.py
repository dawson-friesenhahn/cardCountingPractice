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
        
        self.player_frame= tk.Frame(self.root, bg="green")
        self.player_frame.place(relx=0, rely=0.6, relwidth=0.6, relheight=0.3)
        self.showPlayerTotal= True
        self.playerTotalLabel= ttk.Button(root, text="Player Total: ", command= self.togglePlayerHandTotalLabel)
        self.playerTotalLabel.place(relx=0.6, rely=0.6, relwidth=0.2, relheight=0.05)

        self.dealer_frame= tk.Frame(self.root, bg="green")
        self.dealer_frame.place(relx=0, rely=0, relwidth=0.6, relheight=0.4)
        self.dealerDownCardTk= None
        self.dealerDownCard= None

        self.hitButton= ttk.Button(root, text="Hit", command=self.hit)
        self.hitButton["state"] = "disabled"
        self.hitButton.place(relx=0, rely=0.9, relwidth=0.1, relheight=0.1)
        self.standButton= ttk.Button(root, text="Stand", command=self.stand)
        self.standButton.place(relx=0.1, rely=0.9, relwidth=0.1, relheight=0.1)
        self.dealButton= ttk.Button(root, text= "Deal", command=self.deal)
        self.dealButton.place(relx=0.2, rely=0.9, relwidth=0.1, relheight=0.1) 

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

    def removeChildren(self, widget):
        for child in widget.winfo_children():
            child.destroy()

    def deal(self):
        self.photo_images.clear()
        self.dealerHand.clear()
        self.playerHand.clear()

        self.removeChildren(self.player_frame)
        self.removeChildren(self.dealer_frame)

        
        
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

        #print(f"Parent width, height: {parent_width}, {parent_height}")
        aspect_ratio = img.width / img.height
        # if parent_width / aspect_ratio < parent_height:
        #     new_width = int(parent_width)
        #     new_height = int(new_width / aspect_ratio)
        # else:
        #     new_height = int(parent_height)
        #     new_width = int(new_height * aspect_ratio)

        # print(f"w: {new_width}, h:{new_height}")
        new_width= img.width
        new_height= img.height
        if aspect_ratio < 1: #height is greater than width
            new_height= 100
            new_width= int(100 * aspect_ratio)
        else:
            new_width= 100
            new_height = int(100/aspect_ratio)
        

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
    main_frame = tk.Frame(root, width=500, height=500, bg='green')
    main_frame.pack(fill=tk.BOTH, expand=True)
    bj= Blackjack(main_frame)
    
    
    root.mainloop()
    

if __name__ == "__main__":
    main()