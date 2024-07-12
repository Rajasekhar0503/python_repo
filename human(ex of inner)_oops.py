class human:
    def __init__(self):
        self.name= 'raja'
        self.head= self.head()
        self.brain= self.brain()
    def display(self):
        print('hello',self.name)
        self.head.talk()
        self.brain.think()
    class head:
        def talk(self):
            print('your head is talking.....')
    class brain:
            def think(self):
                print('your brain is thinking?.....')
h=human()
h.display()
