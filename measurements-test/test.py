import numpy as np

x = np.array([1234, 25, 36, 47],np.int16)
x.reshape(-1,4)
y=x

for i in range(10):
    x = np.vstack([x,y])
    y=y-1

with open('test.dat', 'a') as f:
    np.savetxt(f, x, fmt='%d')
    f.close()

print(x.shape)



