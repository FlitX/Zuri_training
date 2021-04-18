class Budget:
    
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
    
    def deposit(self, cash):
        self.amount = self.amount + cash
        return self.amount
    
    def withdraw(self, cash):
        self.amount = self.amount - cash
        return self.amount
    
    def transfer(self, obj, cash):
        self.amount = self.amount - cash
        obj.amount = obj.amount + cash
        pass
    
    def balance(self):
        print(self.category, self.amount)

obj1 = Budget('food', 100)
obj2 = Budget('Entertainment', 400)


obj1.deposit(100)

obj1.balance()

obj1.withdraw(150)

obj1.balance()

obj2.balance()

obj2.transfer(obj1, 200)

obj2.balance()
obj1.balance()