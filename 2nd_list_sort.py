'''
#general method
list1=[(1,'b'),(2,'d'),(3,'c'),(4,'a')]
#output [(4,'a'),(1,'b'),(3,'c'),(2,'d')]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i][1]>list1[j][1]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)
'''

#BY using lamda and sorted funtion
list1=[(1,'b'),(2,'d'),(3,'c'),(4,'a')]
sorted_list1=sorted(list1,key=lambda x:x[1])
print(sorted_list1)

