# https://leetcode.com/problems/valid-parentheses/

def isValid(s: str) -> bool:
    prt={
        "(":")",
        "[":"]",
        "{":"}"
    }
    ckd=[]
    for c in s:
        if c in prt:
            ckd.append(prt[c])
        else:
            if len(ckd)==0:
                return False
            if c!=ckd[-1]:
                return False
            else:
                ckd.pop()

    return not ckd
    
print(isValid("]"))