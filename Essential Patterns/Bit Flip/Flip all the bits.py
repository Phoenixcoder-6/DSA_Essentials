def flip_bits(arr):
    n= len(arr)
    for i in range(n):
        if arr[i]==0:
            arr[i]=1
        elif arr[i]==1:
            arr[i]=0
        else:
            return "Invalid!!"
        
    return arr


arr=[1,0,1,1,1,0]
res= flip_bits(arr)
print(res)