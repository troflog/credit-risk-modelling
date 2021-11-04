import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats._continuous_distns import  norm

p = 0.2
rho = 0.3

def prob_cond_common(p,rho,G):
    num = norm.ppf(p)-np.sqrt(rho)*G
    den = np.sqrt(1-rho)
    yn = np.divide(num,den)
    return norm.cdf(yn)

def common_given_prob(p,rho,x):
    num = -np.sqrt(1-rho)*norm.ppf(x)+norm.ppf(p)
    den = np.sqrt(rho)
    return np.divide(num,den)

def common_given_prob_less_than(p,rho,x):
    num = np.sqrt(1-rho)*norm.ppf(x)-norm.ppf(p)
    den = np.sqrt(rho)
    return np.divide(num,den)

G = -3
print('P(-G) >= x')
for i in range(3):
    G = G-i*2
    x = prob_cond_common(p,rho,G)
    Ga = common_given_prob(p,rho,x)
    Gc = common_given_prob_less_than(p,rho,x)
    print('G = {0:.1f},x={1:.3f}, G<={2:.2f} and G <= {3:.3f}'.format(G,x,Ga,Gc))

G = 3
print('P(-G) >= x')
for i in range(3):
    G = G-i*2
    x = prob_cond_common(p,rho,G)
    Ga = common_given_prob(p,rho,x)
    Gc = common_given_prob_less_than(p,rho,x)
    print('G = {0:.1f},x={1:.3f}, G<={2:.2f} and G <= {3:.3f}'.format(G,x,Ga,Gc))
