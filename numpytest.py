import numpy as np

print('my numpy version: ', np.__version__)

randomList = []
for i in range(1000000):
    n = np.random.randint(1, 20)
    randomList.append(n)
#
print("randomList:", randomList)