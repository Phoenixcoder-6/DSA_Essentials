def updated_array(arr):
    zero=[]
    rest=[]
    for i in arr:
        if i ==0:
            zero.append(i)
        else:
            rest.append(i)

    return rest+zero


arr=[1,2,3,0,7,0,4,0]
res= updated_array(arr)
print(res)
