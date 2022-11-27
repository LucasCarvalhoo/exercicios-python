A = [1, 0, 5, -2, -5, 7]
print(A)
B = A[0], A[1], A[5]
B = list(B)
B = sum(B)
print(B)
A.insert(4, '100')
print(A)
for elemento in A:
    print(elemento)