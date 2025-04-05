def find_zero_sumarray(arr):
    n= len(arr)
    subarray=[]
    for start in range(n):
        total=0
        for end in range(start,n):
            total+= arr[end]
            if total ==0:
                subarray.append((start,end))


    return subarray


arr=[4,2,-3,1,6]
res= find_zero_sumarray(arr)
if res:
    print("Subarrays with 0 sum:")
    for start, end in res:
        print(arr[start:end+1])
else:
    print("No subarray with 0 sum found.")


