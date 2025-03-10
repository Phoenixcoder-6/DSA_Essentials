def subarray(arr,k):
    n= len(arr)
    window_sum= sum(arr[:k])
    max_sum= window_sum
    for i in range(k,n):
        window_sum+= arr[i] - arr[i-k]
        max_sum= max(max_sum,window_sum)
    return max_sum
arr= [-1,2,3,4,5,3,5]
k=4
result= subarray(arr,k)
print("Maximum sum is:", result)