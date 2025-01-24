import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
from scipy import stats


##7
a = np.array([75,69.8,85.7,74,69,83.3,68.9,77.8,72.2,77.4])
b = np.array([85.4,83.1,80.2,74.5,70,81.5,75.4,78,85.4,80.4])
d = b-a
d = d[d!=0]
print("d")
print(d)

n = len(d)
print("n")
print(n)
print("B")
B= len(d[d>0])
print(B)
#n=10000
#p=10/19
#k=0
l1 =scipy.stats.binom.cdf(B,n,1/2)
l2 =1 - scipy.stats.binom.cdf(B-1,n,1/2)
ll = min(scipy.stats.binom.cdf(B,n,1/2),1 - scipy.stats.binom.cdf(B-1,n,1/2))
pval = 2*(ll)
print(ll)
