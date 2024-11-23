t=int(input())
for i in range(t):
    x,m=map(int,input().split(" "))
    count=0

    for i in range(1,m+1):
        val=x ^ i 
        if val!=0 and (x%val==0 or i%val==0):
            count+=1
    print(count)
