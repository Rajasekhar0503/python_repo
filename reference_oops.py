class student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def display(self):
        print('hello my name is:',self.name)
        print('my rollno is:',self.rollno)
        print('my marks are:',self.marks)
s=student('raja',18,92)
s.display()
    

