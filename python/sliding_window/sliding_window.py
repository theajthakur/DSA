arr=[5]



width=1
max=0
current=0

current=sum(arr[:width])
max=current
for x in range(0,len(arr)-width):
    current+=arr[width+x]-arr[x]
    if current>max:
        max=current

    print("max: ", max, "; current: ", current)
    
print(max)