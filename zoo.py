class Africa:
    def __init__(self, animal, action):
        self.animal = animal
        self.action = action
       
    def show(self):
        print("In the African animal zone,there are",self.animal,self.action)

gr = Africa("giraffes","eating leafs")
zb = Africa("zebras","walking")
ot = Africa("ostrich","sleeping")
mk = Africa("meerkats","digging a hole")
gr.show()
zb.show()
ot.show()
mk.show()
class BirdPark:
    def __init__(self, animal, action):
        self.animal = animal
        self.action = action
       
    def show(self):
        print("In the bird park,there is a show of",self.animal,self.action)

pr = BirdPark("parrot","cycling")
o = BirdPark("otter","collecting garbage")
pr.show()
o.show()
class Other:
    def __init__(self, animal, action):
        self.animal = animal
        self.action = action
       
    def show(self):
        print("In other zones,there are",self.animal,self.action)

hp = Other("hippopotamus","floating in the water")
tg = Other("tigers","running")
pd = Other("pandas","eating bamboo")
m = Other("monkeys","climbing a tree")
s = Other("snake","molting")
hp.show()
tg.show()
pd.show()
m.show()
s.show()

class Person:
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def see(self):
        print("My name is",self.name,"And I'm",self.action)

pp = Person("Camp","walking around the zoo")
pp.see()