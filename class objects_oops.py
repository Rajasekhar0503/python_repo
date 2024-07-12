class test:
    count=0
    def __init__(self):
        test.count+=1
    @classmethod
    def no_of_objects(cls):
        print('the number of objects created for test class:',cls.count)
t1=test()
t2=test()
test.no_of_objects()
t3=test()
t4=test()
t5=test()
test.no_of_objects()