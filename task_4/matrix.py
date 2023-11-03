import numpy as np
a=np.array([[1,2,3],[4,5,6]],float)

print(a[0,1])
print(a[1,1])

#print(a,shape)
#print(a,dtype)

#b= np.array(range(18), float)
#b_reshape = b.reshape((2,5))


a= np.array(range(6), float).reshape((2,3))
print(a)
print('\n')
b = a.transpose()
print(b)

import numpy as np
aa = np.array([1,2], int)
bb = np.array([3,4,5], int)
cc = np.array([6,7,8], int)

print(np.concatenate(aa,bb,cc))