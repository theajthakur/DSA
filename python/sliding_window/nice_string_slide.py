def isNice(ss):
    status=0
    for x in range(0, len(ss)):
        status=0
        for y in range(x+1, len(ss)):
            if(abs(ord(ss[x]) - ord(ss[y]))==32):
                status=1
                continue
    if(status):
        return True
    else:
        return False
s="BebjJE"
print(isNice(s))