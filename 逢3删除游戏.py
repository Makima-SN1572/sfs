A = [i for i in range (1,42)]
B = 0
while len(A)>2:
    i = 0
    while i<len(A):
        B += 1
        if B == 3:
            A.remove(A[i])
            B = 0
        else:
            i +=1
print(A)