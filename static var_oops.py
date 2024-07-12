class test:
    a=10
    def __init__(self):
        test.b=20
    def m1(self):
        test.c=30
    @classmethod
    def m2(cls):
        cls.d1=40
        test.d=50
    @staticmethod
    def m3():
        test.e=60
t=test()
t.m1()
t.m2()
t.m3()
test.f=70
print(test.__dict__)