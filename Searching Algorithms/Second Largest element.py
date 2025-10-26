def second_largest(arr):
    arr1= sorted(arr)
    return arr1[-2]

arr=[1,54,23,76]
res= second_largest(arr)
print(res)