f = open("file.txt")
nums=(f.read().split("\n"))

for num in nums:
    tgt=num.split(" ")
    tgtt=num.split("-")
    tgtl=len(tgt)
    if tgtl>1:
        print("invalid", num)
        break
    if(tgtl==1):
        if tgt[0][0]!="(" or tgt[0][-1]!=")":
            print("Invalid", num)
            break
