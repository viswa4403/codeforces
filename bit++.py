n=int(input())
answer=0
for i in range(n):
    string=input()
    if string[1]=="+":
        answer+=1
    else:
        answer-=1
print(answer)
