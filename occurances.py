word=input('enter any word:')
#vowels={'a','e','i','o','u'}
d={}
i=0
for x in word:
    #if x in vowels:
    d[x]=d.get(x,0)+1
    i+=1
for k,v in d.items():
    print(k,'occureds',v,'times')