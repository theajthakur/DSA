nums = [3,2,4]
target=6
map={}
res=[]
for i, num in enumerate(nums):
    complement=target-num
    if complement in map:
        res=[map[complement], i]
        break
    map[num]=i

print(res)
