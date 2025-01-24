import statistics
import numpy as np
import scipy.stats
import pandas as pd
from scipy import stats
import math
#




z=[89,90,86,80,97,81,94,82,87,93,94,84,83,78,98]  
p=0.75
A=[z!=85]
print(A)

n=len(A)
b=len(A[A>85])
print(b)
#d<-pbinom(b,n,1-p)
       # a<-1-pbinom(b-1,n,1-p)
      #  p_value<-2*min(a,d)
      #  p_value
       # B=length
