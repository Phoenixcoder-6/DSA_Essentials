def find_pairs(arr, target):
    result= []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+ arr[j] == target:
                result.append((arr[i],arr[j]))

    return result


arr=[8,7,2,5,3,1]
target=10
res= find_pairs(arr,target)
print(res)
