'''n=int(input('enter a number:'))
a,b=0,1
for i in range(n):
    a,b=b,a+b
    print(b)'''

#functions
def fabinocci_series(limit):
    fab_list=[0,1]
    while len(fab_list)<limit:
        next_fabi=fab_list[-1]+fab_list[-2]
        fab_list.append(next_fabi) 
    return fab_list
limit=int(input("enter fabinocci limit number:"))
fabinocci_numbers=fabinocci_series(limit)
print(fabinocci_numbers)