import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
dq = []
j = 0.01
xd1 = [3.0, 4.7, 0.6, 0.6, 1.7, 11.6, 4.9, 2.2, 3.8, 0.6]
xd = np.random.randn(10)
ypl = 0
for i in range(1000):

    dt = 0.01
    x1 = i * dt + j
    x.append(x1)
    yk = 1

    for k in range(10):
        xm = xd[k - 1]
        yk = yk * (1 / x1) * np.exp(-xm / x1)
    y.append(np.log(yk))
    yp = yk
    if ypl != 0:
        d = (yp - ypl) / dt
    else:
        d = 0
    dq.append(d)
    ypl = yp
loc = np.argmax(y)
loc2 = np.argmax(dq)
yp = x[loc]
print(yp)
print(np.exp(x[loc2]))


plt.plot(x, y)
plt.ylabel("likelyhood")
plt.xlabel("val:")
plt.show()
