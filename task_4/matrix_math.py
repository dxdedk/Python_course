import numpy as np

a = np.array([1,2,3],int)
b = np.array([5,2,6],int)

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

aa = np.array([[1,2],[3,4],[5,6]],float)
bb = np.array([-1,3],float)

print(aa+bb)

cc = np.array([4,9,16,25], int)
print(np.sqrt(cc))

array_for = np.array(range(15),int)
for i in array_for:
    print(i)
print('\nМатрциа:')
array_for_m = np.array(range(15),int).reshape(3,5)
for i in array_for_m:
    print(i)

matrix_a = np.array([[0,1],[2,3]], int)
matrix_b = np.array([2,3], float)
print(np.dot(matrix_b,matrix_a))