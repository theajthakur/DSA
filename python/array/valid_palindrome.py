import re
s = "A man, a plan, a canal: Panama"
letters_only = re.findall(r'[A-Za-z]', s)
result = ''.join(letters_only).lower()
lower=0
upper=len(result)-1

isValid=True
while lower<upper:
    if result[lower]!=result[upper]:
        isValid=False
        break
    lower+=1
    upper-=1

print(isValid == True)