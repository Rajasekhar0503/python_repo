n=int(input('enter no of students:'))
rec={}
i=1
while i<=n:
    name=input('enter student of name:')
    marks=int(input('enter % of marks:'))
    rec[name]=marks
    i+=1
print('name of the student','\t','% of marks')
for x in rec:
    print('\t',x,'\t\t',rec[x])
