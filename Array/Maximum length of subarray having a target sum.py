def maximim_length(arr,target):
    n= len(arr)
    max_length=0
    res=[]
    for i in range(n):
        cur_sum=0
        for j in range(i,n):
            cur_sum += arr[j]
            if cur_sum == target:
                if(j-i+11) > max_length:
                    max_length = j-i+11
                    res= arr[i:j+1]

            elif cur_sum> target:
                break


    return res


arr=[5, 6, -5, 5, 3, 5, 3, -2, 0]
res= maximim_length(arr,8)
print(res)