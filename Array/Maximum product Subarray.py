def max_product_subarray(arr):
    max_prod=arr[0]
    min_prod= arr[0]
    max_prod_so_far= arr[0]

    for i in range(len(arr)):
        num= arr[i]

        if num<0:
            max_prod,min_prod= min_prod,max_prod

        max_prod= max(num, max_prod * num)
        min_prod= min(num, min_prod *num)


        max_prod_so_far= max(max_prod_so_far,max_prod )

    return max_prod_so_far


arr=[2,3,-2,4]

res= max_product_subarray(arr)
print(res)