import  numpy as np
from scipy.stats._continuous_distns import norm
x = norm.ppf(0.3)
y =  norm.cdf(2)
x = np.random.normal(size =  7)
y = 3
for i in range(x.size):
    print(i)
print(x)

