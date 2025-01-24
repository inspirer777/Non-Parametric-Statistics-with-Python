import numpy as np
import tkinter
import math
import statistics
import pandas as pd
# matrix rank
from numpy.linalg import matrix_rank
import numpy.linalg as npl
import qnorm

A = [1,5,7,8,13,15,20,21,23,24,25,27,28,29,30]
B = [2,3,4,6,9,10,11,12,14,16,17,18,19,22,26]
n =len(A)
m =len(B)
N = n+m
C= (B,A)
R = npl.matrix_rank(C)
WB = sum(list(range(1, n)))
print('WB ',WB)
WAB = (WB - n)*(n+1)/2
print('WAB',WAB)
EWB = n*(n+1)/2
VWB=n*m*(n+1)/12
print('VWB',VWB)
vv = WB+(1/2)-(EWB)/math.sqrt(VWB)
pval = qnorm.quantile_normalize(vv)

