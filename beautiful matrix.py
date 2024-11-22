answer=0
nums=[]
for i in range(5):
    temp=list(map(int,input().split(" ")))
    nums.append(temp)

for a in range(5):
    for b in range(5):
        if nums[a][b]==1:
            answer=abs(a-2)+abs(b-2)
            print(answer)
            exit()
