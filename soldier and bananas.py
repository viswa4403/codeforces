k,n,w=map(int,input().split(" "))
cost=0
for i in range(w):
    cost+=k*(i+1)
print(cost-n) if cost>n else print(0)
