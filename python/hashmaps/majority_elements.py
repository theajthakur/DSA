# https://leetcode.com/problems/majority-element/description/

num = [3,3,4]
fr={}

for x in num:
    if(x in fr):
        fr[x]+=1
    else:
        fr[x]=1

res=0
for y in fr:
    if fr[y]==max(fr.values()):
        res=y
        break