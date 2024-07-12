class employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    def display(self):
        print('employee number:',self.eno)
        print('employee name:',self.ename)
        print('employee salary:',self.esal)
class test:
    def modify(emp):
        emp.esal+=8000
        emp.display()
e=employee(101,'raja',18000)
test.modify(e)
