# -*- coding: utf-8 -*-
"""
Created on Tue May  7 18:59:18 2019

@author: Balakrishnan
"""

import numpy as np
import pandas as pd
data=pd.read_csv("Online_Retail.csv")
descriptions_unique = data['Description'].unique()
matrix = pd.DataFrame(data=0, index=descriptions_unique, columns=descriptions_unique)
data_final = data.groupby(['InvoiceNo', 'Description'])
data_final=data_final.size()
groups = data.groupby('InvoiceNo').groups.keys()
groups=list(groups)
for i in groups:
    ind=data_final[i].index
    for i in range(0, len(ind)):
        for j in range(0, len(ind)):
            matrix.loc[ind[i]][ind[j]]=matrix.loc[ind[i]][ind[j]]+1
np.fill_diagonal(matrix.values, 0)

matrix.to_csv("a1.csv", sep=",")