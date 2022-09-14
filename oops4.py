#inheritance and multi inheritance
#super class method

class phone:  #base class/parent class
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price

    def full_name(self):
        return f'{self.brand} {self.model}'

class smart_phone(phone):  #child class
    def __init__(self,brand,model,price,ram,internal_memory):
        #phone.__init__(self,brand,model,price)
        super().__init__(sbrand,model,price)
        self.ram=ram
        self.internal_memory=internal_memory

p1=phone('Nokia','1100',1000)
p2=smart_phone('oneplus','5',300000,'6GB','64GB')

print(p2.full_name())
