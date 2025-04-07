def consecutive_subarray(arr):
    n= len(arr)
    max_length=0
    start_index=0
    for i in range(n):
        seen=set()
        min_val= arr[i]
        max_val= arr[i]

        for j in range(i,n):
            if arr[j] in seen:
                break

            seen.add(arr[j])
            min_val= min(min_val,arr[j])
            max_val= max(max_val,arr[j])

            if max_val- min_val == j-i:
                if (j-i+1)> max_length:
                    max_length= j-i+1
                    start_index= i


    return arr[start_index:start_index+ max_length]



arr=[2, 0, 2, 1, 4, 3, 1, 0]
res= consecutive_subarray(arr)
print(res)







