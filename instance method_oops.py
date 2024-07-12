class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print('hi',self.name)
        print('your marks are:',self.marks)
    def grade(self):
        if self.marks>=60:
            print('congrats you got first rank')
        elif self.marks>=50:
            print('congrats you got second rank')
        elif self.marks>=35:
            print('congrats you got third rank')
        else:
            print('sorry you are failed......enjoy pandagooo....')
n=int(input('enter number of students:'))
for i in range(n):
    name=input('enter name:')
    marks=int(input('enter marks:'))
    s=student(name,marks)
    s.display()
    s.grade()
    print()
