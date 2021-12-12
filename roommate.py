class Guest:
    def __init__(self):
       self.name = input("Enter name : ")

    def date(self):
        self.live = int(input("Enter " + self.name + " lived : "))
        return self.live

class Manager:
    def __init__(self):
        self.bill_period = input("Enter bill period : ")
        self.total_rent = int(input("Enter total rent : "))

    def calculate_rent(self,guest1_live,guest2_live):
        self.guest1_price = int(self.total_rent * (guest1_live / (guest1_live + guest2_live)))
        self.guest2_price = int(self.total_rent * (guest2_live / (guest1_live + guest2_live)))
    
    def show_bill(self,name1,name2):
        print("Bill period : ",self.bill_period)
        print(name1 + " have to pays :",self.guest1_price)
        print(name2 + " have to pays :",self.guest2_price)

guest1 = Guest()
guest2 = Guest()
manager = Manager()
manager.calculate_rent(guest1.date(),guest2.date())
manager.show_bill(guest1.name,guest2.name)