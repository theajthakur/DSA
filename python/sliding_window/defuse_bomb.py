code = [5,7,1,4]
res=[0]*len(code)
k = -2

if k > 0 :
    minsum=sum(code[:k])
    for x in range(0,len(code)):
        minsum+=code[(k+x)%len(code)]-code[x]
        res[x]=minsum

elif k < 0:
    minsum=sum(code[k:])
    print(minsum)
    for x in range(0, len(code)):
        res[x]=minsum
        minsum+=code[x]-code[k+x]

print(res)
