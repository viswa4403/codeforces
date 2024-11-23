word=input()
count=0
for i in range(len(word)):
    if ord(word[i])>=97 and ord(word[i])<=122:
        count+=1

n=len(word)
if n-count>count:
    word=word.upper()
    
else:
    word=word.lower()
print(word)