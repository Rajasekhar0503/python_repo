class p1:
    def m1(self):
        print('parent-1 method')
class p2:
    def m1(self):
        print('parent-2 method')
class c(p1,p2):
    def m2(self):
        print('child method')
c=c()
c.m1()
c.m2()