arr=[82,56,91,87,25,76,56]

width=3
max=0
current=0

max=sum(arr[:width])
    
for x in range(0,len(arr)-width):
    current=max-arr[x]+arr[width+x]
    if current>max:
        max=current


print(max)