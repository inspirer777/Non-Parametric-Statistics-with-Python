import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd
from scipy import stats

import matplotlib.pyplot as plt
x= (10.3,11.2,11.5,11.9,12.8)
y= (10.4,11.8,12.5,12.6,13.8,13.9)
print(stats.kstest(x,y))
#seaborn.ecdfplot(data=None, *, x=None, y=None, hue=None, weights=None, stat='proportion'
#, complementary=False, palette=None,
#  hue_order=None, hue_norm=None, log_scale=None, legend=True, ax=None, **kwargs)
import seaborn as sns
sns.ecdfplot(x)
sns.ecdfplot(y)

plt.show()
