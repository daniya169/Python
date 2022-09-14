#oops--> object orientation programming system
#class
#__init__ method
#how to create varibles
class person:
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
        #self.full_name=fname+' '+lname

    def full_name(self):
        return f'{self.fname} {self.lname}'

p1=person('Chetan','Prakash',31)
p2=person('Anuj','Singh',29)
print(p1.fname)
print(p1.lname)
#print(p1.full_name)
print(p1.full_name())
print(person.full_name(p2))
