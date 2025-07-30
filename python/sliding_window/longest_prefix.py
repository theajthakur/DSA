# https://leetcode.com/problems/longest-common-prefix/

strs = ["flower","flow","flight"]

winsize=len(strs[0])

for str in strs:
    if len(str)<winsize:
        winsize=len(str)


def checkAll(strs, winsize):
    match=strs[0][:winsize]
    for str in strs:
        if str[:winsize]!=match:    
            return checkAll(strs, winsize-1)
    return match

print(checkAll(strs, winsize))