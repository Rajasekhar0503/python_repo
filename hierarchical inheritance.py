class p:
    def m1(self):
        print('parent method')
class c1(p):
    def m2(self):
        print('child-1 method')
class c2(p):
    def m3(self):
        print('child-2 method')
c=c1()
c.m1()
c.m2()
c=c2()
c.m1()
c.m3()