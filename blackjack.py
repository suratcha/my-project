import random
class Deck:
    def __init__(self):
        self.symbol = ["♣","♦","♥","♠"]
        self.point = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = []
        for x in self.symbol:
            for y in self.point:
                self.cards.append(x+y)
        random.shuffle(self.cards)

    def deal(self):
        dealcards = self.cards[0]
        self.cards.remove(self.cards[0])
        return dealcards

class Player:
    def __init__(self,cards):
        self.cards = cards
        print(self.cards)

    def select(self):
        select = input("Select hit/stand : ")
        if select == "hit" :
            self.hit()
        elif select == "stand" :
            pass

    def hit(self):
        self.cards.append(deck.deal())
        print(self.cards)

    def calculate(self):
        self.score = 0
        for cards in self.cards:
            if cards[1:3] == "10" or cards[1:2] == "J" or cards[1:2] == "Q" or cards[1:2] == "K":
                self.score+= 10
            elif cards[1:2] == ("A"):
                 card_value = input("Select a score of 1/11 : ")
                 if card_value == "1":
                    self.score+= 1
                 elif card_value == "11":
                    self.score+= 11
            else :
                self.score+= int(cards[1:2])
    
    def check(self):
        if self.score > 21:
            return "Busted"
        elif self.score <= 21:
            return str(self.score)

def result(point):
    bust = [] 
    all_point = []
    num = 1 
    for b in point:
        if "Bust" in b:
            bust.append("player"+str(num))
            num += 1
        else:
            all_point.append(b+" Player "+str(num))
            num += 1
    if len(bust) > 0: 
        print(str(bust)+" You Busted")
    all_point.sort() 
    print(all_point[-1][2:]+"You Win") 
    
deck = Deck()
player1 = Player([deck.deal(),deck.deal()])
player2 = Player([deck.deal(),deck.deal()])
print("player 1")
player1.select()
player1.calculate()
print("player 2")
player2.select()
player2.calculate()
result([player1.check(),player2.check()])
