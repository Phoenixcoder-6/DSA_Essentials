def count_bit_flips(A,B):
    operations=1
    for i,j in zip(A,B):
        if i!=j:
            operations+=1
    return operations

A="1011"
B="0110"
res= count_bit_flips(A,B)
print("Required operations are:",res)
