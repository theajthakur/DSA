def checkNice(ss):
    if(len(ss)<2):
        return False
    for x in range(1,len(ss)):
        if(abs(ord(ss[x])-ord(ss[x-1]))==32):
            return True
    return False

s="dDzeE"
result=""
res=""
last=""
p=s.lower()
for x in range(0, len(s)):
    if p[x]==last:
        res+=s[x]
    else:
        if len(res)>1 and checkNice(res) :
            result+=res
        else:
            if(len(result)>1):
                break
        res=s[x]

    last=p[x]


if checkNice(res):
    print(result+res)
else:
    print(result)