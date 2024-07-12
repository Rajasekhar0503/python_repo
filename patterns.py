'''n=int(input('enter a value:'))
for i in range(n):
    print((str(n)+' ')*n)'''
'''n=int(input('enter no of rows:'))
for i in range(n):
    print(('A ')*n)'''
n=int(input('enter no of rows:'))
for i in range(n):
    print((chr(65+i)+' ')*n)
'''n=int(input('enter no of rows:'))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=' ')
    print()'''
'''n=int(input('enter no of rows:'))
for i in range(n):
    print(chr((64+n-i)+' ')*n)'''