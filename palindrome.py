str=input("enter str")
revstr=""
for i in str:
    revstr=i+revstr
print("reversed str:",revstr)
if (str==revstr):
    print("the str is palindrome")
else:
    print("the str is not palimdrome") 