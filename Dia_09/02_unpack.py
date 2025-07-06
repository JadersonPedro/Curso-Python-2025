#%%

A = 1
B = 5

print(A)
print(B)

#%%

C = A
A = B
B = C

print(A)
print(B)

#%%

B, A = A, B

print(A)
print(B)

#%%

a, b, *resto = [1, 2, 4, 5, 6, 7, 8, 9, 10, 500]
print(a,b, resto)

#%%

*resto, a, b = 1, 2, 3, 4, 5, 6, 100, 350, 390, 500
print(a,b, resto)

#%%

a, *resto,  b = 1, 2, 3, 4, 5, 6, 100, 350, 390, 500
print(a,b, resto)

#%%

def soma(a, *args):
    total = a + sum(args)
    return total

soma(1,2,4,7)

#%%

def soma_quatro(a, b, c, d):
    return a+b+c+d

values = [1,2,3,4]
soma_quatro(*values)

#%%

soma(*values)
