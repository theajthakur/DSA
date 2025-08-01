s = "(()())(())(()(()))"
stack=[]
res=""
for c in s:
    if c==")":
        stack.pop()
    if len(stack)>=1:
        res+=(c)
    if c=="(":
        stack.append("(")



print(res)