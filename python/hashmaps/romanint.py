# https://leetcode.com/problems/roman-to-integer/description/

s="MCMXCIV"

roman={}
roman["I"]=1
roman["V"]=5
roman["X"]=10
roman["L"]=50
roman["C"]=100
roman["D"]=500
roman["M"]=1000

res=0
last=0

for c in s:
    num=roman[c]
    if num>last:
        res+=num-2*last
    else:
        res+=num
    last=num

print(res)