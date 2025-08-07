def product_of_array(arr):
    res=[]
    for i in range(len(arr)):
        left_product=1
        right_product=1

        for j in range(i):
            left_product*= arr[j]

        for k in range(i+1, len(arr)):
            right_product *= arr[k]

        res.append(left_product * right_product)

    return res

arr=[1,2,3,4]
result= product_of_array(arr)
print(result)


