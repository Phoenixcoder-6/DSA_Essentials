def sort_array(arr):
    left=0
    right=len(arr)-1

    while left<right:
        if arr[left]==1 and arr[right] ==0:
            arr[left],arr[right] = arr[right],arr[left]
            left+=1
            right-=1

        if arr[left] ==0:
            left+=1
        if arr[right] ==1:
            right-=1


    return arr

arr=[0,1,0,1,1,1,1,1,0,0,0,0,0]
res= sort_array(arr)
print(res)
