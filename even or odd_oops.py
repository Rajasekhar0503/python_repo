class EvenOddChecker:
    def __init__(self,number):
        self.num=number
    def even_num(self):
        return self.num%2==0
    def odd_num(self):
        return not self.even_num()
#while True:
number=int(input("enter a number:"))
checker=EvenOddChecker(number)
if checker.even_num():
    print(f"{number} is even")
else:
    print(f"{number} is odd")