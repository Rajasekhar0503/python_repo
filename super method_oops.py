class p:
    a=10
    def __init__(self):
        self.b=20
    def m1(self):
        print('parent instance method')
    @classmethod
    def m2(cls):
        print('parent class method')
    @staticmethod
    def m3():
        print('parent static method')
class c(p):
    def __init__(self):
        super().__init__()
        print(self.a)
        print(self.b)
        super().m1()
        super().m2()
        super().m3()
c=c()