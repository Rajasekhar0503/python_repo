words='virat kohli is my favourite player'
w=[]
words=words.split()
for word in words:
    l=[word.upper(),len(word)]
    w.append(l)
print(w)