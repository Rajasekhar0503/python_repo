class outer:
    def __init__(self):
        print('outer class object creation')
    class inner:
        def __init__(self):
            print('inner class object creation')
        def m1(self):
            print('innerclass method')
outer().inner().m1()