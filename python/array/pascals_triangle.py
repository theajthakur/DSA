n=5
res=[]
for x in range(0,5):
    tmp=[1]
    for y in range(0,x):
        digit=y
        if y==x-1:
            digit=1
        else:
            digit=res[x-1][y]+res[x-1][y+1]
        tmp.append(digit)
    res.append(tmp)
print(res)