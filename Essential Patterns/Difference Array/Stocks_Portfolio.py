def stocks_update(stocks, updates):
    n= len(stocks)
    gradient= [0] * (n+1)

    for l,r,val in updates:
        gradient[l] += val
        if r+1 < len(gradient):
            gradient[r+1] -=val


    #construct the full array

    updated_stocks= stocks[:]
    current_change= 0
    for i in range(n):
        current_change+= gradient[i]
        updated_stocks[i] += current_change

    return updated_stocks


stocks=[15,10,5,20,40]
updates= [(1,3,10),(1,4,5)]
print(stocks_update(stocks, updates))
