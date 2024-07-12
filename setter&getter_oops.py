class student:
    def set_name(self,name):
        self.name =name
    def get_name(self):
        return self.name
    def set_marks(self,marks):
        self.marks =marks
    def get_marks(self):
        return self.marks
l=[]
n=int(input('enter no of students:'))
for i in range(n):
    s=student()
    name=input('enter name:')
    s.set_name(name)
    marks=int(input('enter marks:'))
    s.set_marks(marks)
for s in l:
    print('student name:',s.get_name)
    print('student marks:',s.get_marks)
