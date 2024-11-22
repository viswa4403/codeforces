m,n = map(int,input().split(" "))
prod=m*n
if prod%2==0:
    print(prod//2)
else:
    print((prod-1)//2)
    