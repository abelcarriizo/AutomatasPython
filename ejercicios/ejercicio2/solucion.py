#Calentamiento
A = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
B = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

union = A.union(B)
interseccion = A.intersection(B)
BA = {a + b for a in A for b in B}
A_pow1 = A
B_pow3 = {b * 3 for b in B}

print(f'Union: {union}')
print(f'Interseccion: {len(interseccion)}')
#print(f'Concatenacion: {BA}')
print(f'A^1: {A}')
print(f'B^3: {B_pow3}')
print('A^0 = ε')
B_star = {''} | {b for i in range(1, 5) for b in B}
#print(f'B*: {B_star}')
B_union_A_star = {b + a for a in A for b in B_star}
print(f'B (A U B): {B_union_A_star}')
