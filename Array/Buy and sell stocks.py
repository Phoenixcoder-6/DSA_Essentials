def stock(arr):
    min_price= min(arr)
    min_price_index= arr.index (min_price)
    rest= arr[min_price_index+1 : ]
    max_price= max(rest)
    max_price_index= arr.index(max_price)

    return min_price_index, max_price_index


arr=[2,5,3,7,8,2]
buy,sell= stock(arr)
print("Stock should buy on day : ", buy+1, " and sell on day:" , sell+1)
