import numpy as np
import pylab as plt

data = []

heltz = 12500.0

x = []
y = []

with  open("muishiki1.dat", "r") as f:
    for line in f:
        t, d = map(float, line.split(' '))
        
        if(4.5 <= t <= 5.6):
            data.append(d)
N = len(data)

hammingWindow = np.hamming(N)
hanningWindow = np.hanning(N)
bartlettWindow = np.bartlett(N)
blackmanWindow = np.blackman(N)

tran = np.fft.fft(data*hammingWindow)


x = []
y = []
tmpx = 0
cnt = 0
with open("muishiki1_trans.dat", "w") as f:
    for d in tran:
        tmpx = heltz / (len(tran)) * cnt
        cnt += 1
        if(tmpx > 200):continue

        x.append(tmpx)
        y.append(np.abs(d))
        f.write("%3.10f, %3.10f\n"%(tmpx, np.abs(d)))

print len(x)
plt.plot(x, y, color = "k")

plt.show()

