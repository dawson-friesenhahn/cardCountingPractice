from .Card import Card, CARD_NUM_TO_CARD_NAME
import tkinter as tk
from PIL import Image, ImageTk

class Hand:
    def __init__(self, root= None):
        self.cards= []
        self.root= root
        if root is not None:
            self.photoImages= []

            self.mainFrame= tk.Frame(root, bg="green")
            self.cardsFrame= tk.Frame(self.mainFrame, bg="green")
            self.cardsFrame.place(relx= 0, rely= 0, relheight=1, relwidth=0.7)

            self.handTotalVisible= False
            self.handTotal = tk.Button(self.mainFrame, command=self.showHandTotal)
            self.handTotal.place(relx=0.7, rely= 0.4, relheight=0.2, relwidth=0.3)
            self.updateHandTotalLabel()

    def makeFirstCardFaceUp(self):
        self.cards[0].show_back= False
        img= self.getTkImageForCard(self.cards[0])
        self.cardsFrame.winfo_children()[0].config(image= img)
        self.photoImages.append(img)

    def showHandTotal(self):
        if self.root is None:
            RuntimeError("No root was specified when you created the hand, you messed up")
        self.handTotalVisible= not self.handTotalVisible

        for card in self.cards:
            if card.show_back:
                self.handTotalVisible= False
                break

        self.updateHandTotalLabel()

    def updateHandTotalLabel(self):
        if self.root is not None and self.handTotalVisible:
            self.handTotal.config(text= f"Total: {self.calculateTotal()}")
        else:
            self.handTotal.config(text= "Show Hand Total")

    def getTkImageForCard(self, card):
        imgName= "./Images/" + card.getFullName() + ".png"
        #print(imgName)
        img= Image.open(imgName)

        # Resize the image to fit the size of the parent frame
        parent_width = self.cardsFrame.winfo_width()
        parent_height = self.cardsFrame.winfo_height()

        # print(f"Parent width, height: {parent_width}, {parent_height}")
        aspect_ratio = img.width / img.height
        # if parent_width / aspect_ratio < parent_height:
        #     new_width = int(parent_width/7)
        #     new_height = int(new_width / aspect_ratio)
        # else:
        #     new_height = int(parent_height)
        #     new_width = int(new_height * aspect_ratio/7)

    
        new_width= img.width
        new_height= img.height
        if aspect_ratio < 1: #height is greater than width
            new_height= parent_height
            new_width= int(parent_height * aspect_ratio)
        else:
            print("idk cards should be long and skinny bro")
        img = img.resize((new_width, new_height), Image.ANTIALIAS)

        return ImageTk.PhotoImage(img)


    def addCardToTk(self, card):
        if self.root is None:
            return
        tkImage= self.getTkImageForCard(card)
        tkCard = tk.Label(self.cardsFrame, image=tkImage)
        x= (len(self.cardsFrame.winfo_children()) -1) * 0.1
        tkCard.place(relx=x, rely= 0, relheight=1)
        # Keep a reference to the PhotoImage object
        self.photoImages.append(tkImage)
        if card.show_back:
            self.handTotalVisible= False
        self.updateHandTotalLabel()
        #self.root.update()
        return tkCard
    
    def append(self, newCard):
        self.cards.append(newCard)
        if self.root is not None:
            self.addCardToTk(newCard)

    def clear(self):
        self.cards.clear()
        if self.root is not None:
            self.photoImages.clear()
            for child in self.cardsFrame.winfo_children():
                child.destroy()


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
        if (num_aces > 0):
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
