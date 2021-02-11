import numpy as np
import matplotlib.pyplot as plt


np.random.seed(123)

all_walks = []
for x in range(10):
    random_walk = [0]
    for x in range(100):
        coin = np.random.randint(0, 2)
        random_walk.append(random_walk[x] + coin)
    all_walks.append(random_walk)


# np_aw = np.array(all_walks)
# plt.plot(np_aw)
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()


# ends = np_aw_t[-1, :]
# print(len(ends[ends >= 5]))
