def check_subarrays(arr):
    n= len(arr)
    subarrays=[]
    for start in range(n):
        total=0
        for end in range(start,n):
            total+= arr[end]
            if total==0:
                subarrays.append((start,end))
    return subarrays


arr=[2,4,-3,-1,0,4]
res= check_subarrays(arr)

if res:
    print("Subarray exists.")
    for start,end in res:
        print(arr[start:end+1])
else:
    print("Subarray doesn't exists.")


 