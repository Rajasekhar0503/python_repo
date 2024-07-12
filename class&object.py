'''
class firstclass:
    attribute1=10
    attribute2=20
obj=firstclass()
print(obj.attribute1)
print(obj.attribute2)
'''

class firstapp:
    def __init__(self,name,age,phonenumber,collegename,address,branch):
        self.name=name
        self.age=age
        self.phone=phonenumber
        self.collegename=collegename
        self.address=address
        self.branch=branch
    def display(self):
        print('my name is',self.name)
        print("my age is ",self.age)
        print("my phone numner is",self.phone)
    def sencondmethod(self):
        print('college name :',self.collegename)
        print("address :",self.address)
        print("branch:",self.branch)

s=firstapp('siva',25,6304231562,'nbkr','tirupati','civil')
s.display()
s.sencondmethod()