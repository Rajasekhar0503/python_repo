class test:
    a=10
    def __init__(self):
        print(test.a)
        print(self.a)
    def m1(self):
        print(test.a)
        print(self.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(test.a)
    @staticmethod
    def m3():
        print(test.a)
t=test()
t.m1()
t.m2()
t.m3()
print(test.a)
