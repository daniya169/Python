#instance count
#class method
class laptop:
    count_instance=0
    def __init__(self,brand,model,price):
        laptop.count_instance += 1
        self.brand=brand
        self.model=model
        self.price=price
        
    @classmethod
    def instance_count(cls):
        return f'you have created {cls.count_instance} instance of laptop class'


l1=laptop('HP','XTU456',56000)
l2=laptop('DELL','Visto486',48000)
#l3=laptop('DELL','486',50000)
#'you have created 4 instance of laptop class'
print(laptop.instance_count())
