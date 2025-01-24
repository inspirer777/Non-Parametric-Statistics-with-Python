import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
from scipy import stats

#
from scipy.stats import friedmanchisquare

## 11
x1=(3,4,3)
x2 = (4,3,4)
x3 = (2,2,1)
x4 = (1,1,2)
X = [x1,x2,x3,x4]

print(X)
df =pd.DataFrame(X)
print(df)


stat, p = friedmanchisquare(x1, x2, x3,x4)
print('Statistics=%.3f, p=%.3f' % (stat, p))
# interpret
alpha = 0.05
if p > alpha:
	print('Same distributions (fail to reject H0)')
else:
	print('Different distributions (reject H0)')

#friedman.test(x)
