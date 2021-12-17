import random
rx = random.randint(0,10)
ry = random.randint(0,10)
rx1 = random.randint(10,20)
ry1 = random.randint(10,20)
print(rx,ry,rx1,ry1)
class RecGame:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.allarea = (rx1 - rx) * (ry1 - ry)
        print(self.allarea)

    def check(self,px,py):
        if  self.x2 > px > self.x1 and self.y2 > py > self.y1 :
            return True
        else:
            return False
    
    def checkarea(self,area):
        self.area = area
        if self.area == self.allarea :
            return True
        else:
            return False

    def result(self):
        if self.check(x,y) == True:
            print("you win")
        else:
            print("you lose")
        if self.checkarea(Area) == True:
            print("you guess correct")
        else:
            print("you guess wrong")

x = int(input("Enter x : "))
y = int(input("Enter y : "))
Area = int(input("Guess the area : "))
rec = RecGame(rx,ry,rx1,ry1)
rec.result()