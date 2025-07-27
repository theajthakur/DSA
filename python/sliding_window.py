arr=[3,9,25,31,55]

width=3
max=0
for x in range(0,len(arr)-width+1):
    current=0
    for y in range(0,3):
        current+=arr[y+x]

    if max<current:
        max=current

print("Max is ",max)