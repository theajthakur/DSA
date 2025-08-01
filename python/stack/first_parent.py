s = "(()(()))"

count=0
res=""
for c in s:
    if c==")":
        count-=1
    if count:
        res+=c
    if c=="(":
        count+=1



print(res)