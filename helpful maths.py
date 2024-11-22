string=input()
nums=[]
for i in range(0,len(string),2):
    nums.append(int(string[i]))
nums.sort()
answer=""
answer+=str(nums[0])
for i in range(1,len(nums)):
    answer+="+"
    answer+=str(nums[i])
print(answer)