code = [5,7,1,4]
k = 3
code2=[*code,*code]

if k > 0 :
    minsum=sum(code[:k])
    for x in range(0, len(code)):
        minsum+=code2[k+x]-code2[x]
        code[x]=minsum
elif k < 0:
    minsum=sum(code[k:])
    print(minsum)
    code[0]=minsum
    for x in range(1, len(code)):
        minsum+=code2[len(code)-1+x]-code2[len(code)-1+k+x]
        code[x]=minsum
else:
    code=[0]*len(code)

print(code)
