from abc import *
class test:
    @abstractmethod
    def m1(self):
        print('Hi')
t=test()
t.m1()
