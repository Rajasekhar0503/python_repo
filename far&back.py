s=input('enter some string:')
n=len(s)
i=0
print('forward direction:',s)
while i<n:
    print(end='')
    i+=1
print('backward direction:',s[::-1])
i=-1
while i>=-n:
    print(end='')
    i-=1