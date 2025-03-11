def first_negative_number(arr,k):
    n= len(arr)
    neg_arr=[]
    left=0

    for right in range(k-1,n):
        while left < right and arr[left] >=0:
            left +=1
        if arr[left] < 0:
            neg_arr.append(arr[left])
        else:
            neg_arr.append(0)

        if left== right-k +1:
            left+=1

    return neg_arr

arr=[12,-1,-7,8,-15,30,16,28]
k=3
result= first_negative_number(arr,k)
print(result)