def missing_number(arr):
    n=max(arr)
    hash=[0]*(n+1)
    res=[]

    for i in range(len(arr)):
        hash[arr[i]] +=1
    #find missing number
    for i in range(1,n+1):
        if hash[i] ==0:
            res.append(i)              
    return res if res else -1

arr=[1,2,3,4,7,8]
res= missing_number(arr)
print(res)