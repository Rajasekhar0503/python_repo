n=int(input("enter a number:"))
k=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**k
    temp//=10
if n==sum:
    print(n,"is an armstrong number")
else:
    print(n,"is not an armstrong number")

